// NOVA 013 — opt-in cloud transport. No remote calls unless the owner supplies
// a public publishable/anon key AND explicitly signs in and requests a sync.
(() => {
  'use strict';
  const CFG = window.NOVA_CLOUD_CONFIG || null;
  const configured = !!(CFG && /^https:\/\/[a-z0-9.-]+\.supabase\.co$/i.test(CFG.url || '') && typeof CFG.publishableKey === 'string' && CFG.publishableKey.length >= 20);
  const ORIGIN = configured ? CFG.url.replace(/\/$/,'') : '';
  const BUCKET = 'nova-audio';
  const TOKEN_KEY = 'nova013.session.v1';
  const MAX_SONG = 25 * 1048576;
  const MAX_BATCH = 120 * 1048576;
  let token = null, userId = null, busy = false;
  try { const saved = JSON.parse(sessionStorage.getItem(TOKEN_KEY) || 'null'); if(saved?.token && saved?.userId){token=saved.token;userId=saved.userId;} } catch {}
  const element = id => document.getElementById(id);
  const message = text => {const e=element('nova-cloud-feedback');if(e)e.textContent=text;};
  function safeErr(e){return (e?.message||'Ошибка сети').slice(0,190).replace(/[\r\n]/g,' ')}
  function show(){
    const status=element('nova-cloud-status');if(status)status.textContent = !configured ? 'Не подключено: файлы находятся только на этом устройстве' : !token ? 'Облако настроено, требуется вход' : 'Выполнен вход · синхронизация только вручную';
    const form=element('nova-cloud-auth');if(form)form.hidden=!configured||!!token;
    const controls=element('nova-cloud-controls');if(controls)controls.hidden=!configured||!token;
  }
  function sessionSet(value){token=value?.access_token||null;userId=value?.user?.id||null;try{if(token && userId)sessionStorage.setItem(TOKEN_KEY,JSON.stringify({token,userId}));else sessionStorage.removeItem(TOKEN_KEY)}catch{}show()}
  function requireConfig(){if(!configured)throw Error('Облако не настроено владельцем NOVA. Локальная медиатека доступна.');if(!isSecureContext)throw Error('Для облака нужен HTTPS.');}
  async function request(path,{method='GET',body,auth=true,headers={}}={}){
    requireConfig();
    const h={'apikey':CFG.publishableKey,...headers};
    if(auth){if(!token)throw Error('Сначала войди в облачную медиатеку');h.Authorization='Bearer '+token}
    let r;
    try{r=await fetch(ORIGIN+path,{method,headers:h,body,mode:'cors',cache:'no-store',credentials:'omit'})}catch{throw Error('Нет соединения с облачным сервером')}
    if(!r.ok){ if(r.status===401)throw Error('Сессия устарела: выйди и войди заново');if(r.status===403)throw Error('Доступ запрещён: проверь RLS/права');if(r.status===409)throw Error('Запись уже существует');if(r.status===413)throw Error('Файл превышает лимит хранилища');throw Error(`Сервер ответил ${r.status}`)}
    return r;
  }
  async function login(signUp){
    const email=(element('nova-cloud-email')?.value||'').trim(); const pwd=element('nova-cloud-password')?.value||'';
    if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)||pwd.length<10)throw Error('Введи email и пароль не короче 10 символов');
    const path=signUp?'/auth/v1/signup':'/auth/v1/token?grant_type=password';
    const r=await request(path,{method:'POST',auth:false,headers:{'content-type':'application/json'},body:JSON.stringify({email,password:pwd})});
    const data=await r.json();
    if(!data.access_token){message('Проверь почту и подтверди адрес, затем войди в NOVA.');return}
    if(!data.user?.id)throw Error('Сервер не подтвердил профиль');
    sessionSet(data);element('nova-cloud-password').value='';message('Вход подтверждён. Можно загрузить песни в приватную медиатеку.');
  }
  function remotePath(songId){return `${encodeURIComponent(userId)}/${encodeURIComponent(songId)}`}
  const META_FIELDS=['id','title','genre','mood','voice','idea','lyrics','caption','created','updated','favorite','source','sourceFileName','rootProjectId','duration','mediaType','audioSha256'];
  function metaFrom(song){const out={};for(const f of META_FIELDS)if(song[f]!==undefined && song[f]!==null)out[f]=song[f];return out}
  function validateRemote(raw){
    if(!raw || typeof raw!=='object' || typeof raw.song_id!=='string' || raw.song_id.length>128 || !/^[A-Za-z0-9_.-]+$/.test(raw.song_id))throw Error('Недопустимый ID записи в облаке');
    if(!raw.payload || typeof raw.payload!=='object' || raw.payload.id!==raw.song_id || typeof raw.payload.title!=='string' || raw.payload.title.length>150)throw Error('Повреждены метаданные песни');
    if(raw.audio_sha256!==null && raw.audio_sha256!==undefined && !/^[a-f0-9]{64}$/.test(raw.audio_sha256))throw Error('Неверная контрольная сумма аудио');
    if(raw.audio_path && raw.audio_path!==remotePath(raw.song_id))throw Error('Недопустимый путь аудио');
    return true;
  }
  async function cloudList(){let rows=[];for(let off=0;off<5000;off+=100){const r=await request('/rest/v1/nova_songs?select=song_id,payload,audio_path,audio_sha256&order=song_id.asc&limit=100&offset='+off);const part=await r.json();if(!Array.isArray(part))throw Error('Некорректный ответ базы');part.forEach(validateRemote);rows.push(...part);if(part.length<100)break;if(off>=4900)throw Error('Лимит списка 5000, обратись к администратору')}return rows}
  async function hexBlob(blob){if(!crypto?.subtle)throw Error('SHA-256 недоступен');const h=await crypto.subtle.digest('SHA-256',await blob.arrayBuffer());return Array.from(new Uint8Array(h),b=>b.toString(16).padStart(2,'0')).join('')}
  async function push(){
    const current=await cloudList();const ids=new Map(current.map(r=>[r.song_id,r]));
    const local=await getAll();let uploaded=0,skipped=0,conflicts=0,totalBytes=0;
    for(const song of local){
      if(!song.id||!/^[A-Za-z0-9_.-]+$/.test(song.id)||song.id.length>128||song.id.startsWith('__nova')){skipped++;continue}
      const old=ids.get(song.id);if(old){
        const localMeta=metaFrom(song); const remoteMeta=old.payload || {};
        const changed=Object.keys(localMeta).some(k=>JSON.stringify(localMeta[k])!==JSON.stringify(remoteMeta[k]));
        if(changed || ((old.audio_sha256||null)!==(song.audioSha256||null) && song.audioSha256))conflicts++;else skipped++;
        continue;
      }
      let audioPath=null,sha=null;
      if(song.audio){
        if(song.audio.size>MAX_SONG)throw Error(`Трек ${song.title}: аудио больше 25 МБ — скачай оригинал отдельно`);
        totalBytes+=song.audio.size;if(totalBytes>MAX_BATCH)throw Error('Лимит пакета 120 МБ, загружено '+uploaded+' треков. Повтори позднее.');
        sha=await hexBlob(song.audio);audioPath=remotePath(song.id);
        await request('/storage/v1/object/'+BUCKET+'/'+audioPath,{method:'POST',body:song.audio,headers:{'content-type':song.audio.type||'audio/mp4','x-upsert':'false'}});
      }
      await request('/rest/v1/nova_songs',{method:'POST',headers:{'content-type':'application/json','Prefer':'return=minimal'},body:JSON.stringify({user_id:userId,song_id:song.id,payload:metaFrom(song),audio_path:audioPath,audio_sha256:sha})});
      uploaded++;
    }
    message(`Загрузка завершена: ${uploaded} новых, ${skipped} пропущено, ${conflicts} конфликтов. Оригиналы не удалялись.`);
  }
  async function pull(){
    const remote=await cloudList();const local=await getAll();const ids=new Map(local.map(s=>[s.id,s]));
    const next=[];let conflicts=0,skipped=0,size=0;
    for(const r of remote){
      if(ids.has(r.song_id)){const old=ids.get(r.song_id);if(old.audioSha256&&r.audio_sha256&&old.audioSha256!==r.audio_sha256)conflicts++;else skipped++;continue}
      const row={...r.payload,id:r.song_id};delete row.audioBase64;
      if(r.audio_path){
        const response=await request('/storage/v1/object/authenticated/'+BUCKET+'/'+r.audio_path);
        const blob=await response.blob();size+=blob.size;
        if(blob.size>MAX_SONG||size>MAX_BATCH)throw Error('Лимит скачивания 120 МБ: локальная медиатека не изменена');
        const sha=await hexBlob(blob);if(sha!==r.audio_sha256)throw Error('Ошибка SHA-256: локальная медиатека не изменена');
        row.audio=blob;row.audioSha256=sha;
      }
      next.push(row)
    }
    // Atomic insertion: validated items or nothing. Never overwrite local songs.
    await putBatchAtomic(next);
    await reload();render();show();
    message(`Загружено ${next.length} новых песен, ${skipped} уже есть, ${conflicts} конфликтов. Существующие треки не изменены.`);
  }
  async function perform(action){if(busy)return;busy=true;const controls=element('nova-cloud-controls');if(controls)controls.style.opacity='.65';message('Выполняется проверка…');try{
    if(action==='signup')await login(true);else if(action==='login')await login(false);else if(action==='logout'){sessionSet(null);message('Выход. Музыка осталась на устройстве.')}else if(action==='push')await push();else if(action==='pull')await pull();
  }catch(e){message('Не выполнено: '+safeErr(e))}finally{busy=false;if(controls)controls.style.opacity='';show()}}
  const BASE_STUDIO=studio;
  studio=function(){return BASE_STUDIO()+`<section class="settings-block nova-cloud-block" id="nova-cloud-block" aria-label="Облачная медиатека">
    <h3>Общая медиатека Mac и iPhone</h3>
    <p id="nova-cloud-status">Не подключено — песни хранятся только в этом браузере.</p>
    <p class="smallprint">NOVA не отправляет аудио в облако автоматически. Когда владелец подключит приватное хранилище, можно войти и вручную синхронизировать новые записи. Старые треки никогда не перезаписываются.</p>
    <div id="nova-cloud-auth" hidden><div class="nova-cloud-fields"><label>Email <input id="nova-cloud-email" type="email" autocomplete="email" placeholder="email@example.com"></label><label>Пароль <input id="nova-cloud-password" type="password" autocomplete="current-password" placeholder="Не менее 10 символов"></label></div><div class="btnrow"><button class="cta primary" type="button" data-nova-sync="login">Войти</button><button class="cta secondary" type="button" data-nova-sync="signup">Создать профиль</button></div></div>
    <div id="nova-cloud-controls" hidden><div class="btnrow"><button class="cta primary" type="button" data-nova-sync="push">Загрузить новые песни в облако</button><button class="cta secondary" type="button" data-nova-sync="pull">Скачать новые песни на устройство</button><button class="cta ghost" type="button" data-nova-sync="logout">Выйти</button></div></div>
    <p id="nova-cloud-feedback" class="smallprint" role="status" aria-live="polite"></p>
  </section>`};
  document.addEventListener('click',e=>{const btn=e.target.closest('[data-nova-sync]');if(btn){e.preventDefault();e.stopPropagation();perform(btn.dataset.novaSync)}},true);
  document.addEventListener('DOMContentLoaded',()=>setTimeout(show,40));
  const originalRender=render;
  render=function(){originalRender();show()};
  window.NOVA_SYNC_STATUS=()=>({configured,signedIn:!!token});
})();
