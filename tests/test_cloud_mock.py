from pathlib import Path
from playwright.sync_api import sync_playwright
from hashlib import sha256
import re,json
root=Path(__file__).resolve().parent.parent
html=(root/'index.html').read_text()
# Test transport against a fake Supabase HTTP server; no real music, tokens or accounts.
config='window.NOVA_CLOUD_CONFIG = {url:"https://example.supabase.co",publishableKey:"public-mock-publishable-key-only"};'
html=re.sub(r'window\.NOVA_CLOUD_CONFIG\s*=\s*Object\.freeze\(\{.*?\}\);',config,html,flags=re.S)
assert config in html
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True)
 page=browser.new_page(viewport={'width':390,'height':844})
 failures=[];page.on('pageerror',lambda e:failures.append(str(e)))
 page.set_content(html,wait_until='domcontentloaded')
 page.evaluate("""() => {
    Object.defineProperty(window,'isSecureContext',{value:true,configurable:true}); Object.defineProperty(window,'crypto',{configurable:true,value:{subtle:{digest:async(_a,buf)=>{const v=new Uint8Array(buf);const h=new Uint8Array(32);for(let i=0;i<v.length;i++)h[i%32]=(h[i%32]+v[i]+i)%256;return h.buffer}}}}); window.mockSongs=[];window.mockCloud=[];window.mockBlobs={};window.mockCalls=[];
    getAll = async () => window.mockSongs;
    putBatchAtomic = async (rows) => {for(const row of rows) if(window.mockSongs.some(s=>s.id===row.id))throw Error('Duplicate'); window.mockSongs.push(...rows)};
    reload = async () => {state.songs=window.mockSongs};
    window.fetch = async (url,opts={}) => {
      window.mockCalls.push([url, opts.method||'GET']);
      const json=(v,s=200)=>new Response(JSON.stringify(v),{status:s,headers:{'content-type':'application/json'}});
      if(url.includes('/auth/v1/token'))return json({access_token:'synthetic-verified-token',user:{id:'11111111-1111-4111-8111-111111111111'}});
      if(url.includes('/rest/v1/nova_songs?'))return json(window.mockCloud);
      if(url.endsWith('/rest/v1/nova_songs')&&opts.method==='POST'){
         window.mockCloud.push(JSON.parse(opts.body));return json(null,201)
      }
      if(url.includes('/storage/v1/object/authenticated/')){
        const key=url.split('/nova-audio/')[1];return new Response(window.mockBlobs[key],{status:200,headers:{'content-type':'audio/wav'}});
      }
      if(url.includes('/storage/v1/object/nova-audio/')&&opts.method==='POST'){
        const key=url.split('/nova-audio/')[1];if(window.mockBlobs[key])return json({code:'ResourceAlreadyExists'},409);window.mockBlobs[key]=opts.body;return json({Key:key},200);
      }
      return json({error:'Unknown test endpoint'},404);
    };
    go('studio');
  }""")
 page.wait_for_timeout(100)
 page.locator('#nova-cloud-email').fill('synthetic@example.com')
 page.locator('#nova-cloud-password').fill('sample-long-test-password')
 page.locator('[data-nova-sync="login"]').click()
 page.wait_for_timeout(130)
 print('LOGIN DEBUG',page.evaluate('({status:NOVA_SYNC_STATUS(), feedback:document.getElementById("nova-cloud-feedback")?.innerText,secure:isSecureContext,loginhtml:document.getElementById("nova-cloud-auth")?.hidden, err:mockCalls})'))
 assert page.evaluate('NOVA_SYNC_STATUS().signedIn'), 'Sign-in was not accepted'
 # Non-destructive cloud push of a synthetic WAV-like blob.
 page.evaluate("""async () => {
   const body=new Uint8Array(9000); const header='RIFF';for(let i=0;i<4;i++)body[i]=header.charCodeAt(i);
   window.mockSongs=[{id:'test-song-013',title:'Синтетический трек',genre:'Pop',created:1,audio:new Blob([body],{type:'audio/wav'})}];
   state.songs=window.mockSongs;
 }""")
 page.locator('[data-nova-sync="push"]').click()
 page.wait_for_timeout(350)
 got=page.evaluate('({meta:mockCloud.length,blob:Object.keys(mockBlobs).length,text:document.getElementById("nova-cloud-feedback").innerText,calls:mockCalls.length})')
 print('PUSH',got)
 assert got['meta']==1 and got['blob']==1,got
 page.locator('[data-nova-sync="push"]').click();page.wait_for_timeout(250)
 assert page.evaluate('mockCloud.length')==1
 # Simulate another device with empty local library, download the same track.
 page.evaluate('window.mockSongs=[];state.songs=[]')
 page.locator('[data-nova-sync="pull"]').click();page.wait_for_timeout(400)
 result=page.evaluate('({len:mockSongs.length,withBlob:mockSongs[0]?.audio instanceof Blob,title:mockSongs[0]?.title,text:document.getElementById("nova-cloud-feedback").innerText})')
 print('PULL',result)
 assert result['len']==1 and result['withBlob'] and result['title']=='Синтетический трек',result
 # Fail-closed when cloud audio differs from saved SHA: no local addition.
 page.evaluate('''() => {window.mockSongs=[];state.songs=[];const key=Object.keys(window.mockBlobs)[0];window.mockBlobs[key]=new Blob([new Uint8Array(9500)],{type:'audio/wav'})}''')
 page.locator('[data-nova-sync="pull"]').click();page.wait_for_timeout(320)
 corruption=page.evaluate('({local:mockSongs.length,text:document.getElementById("nova-cloud-feedback").innerText})')
 print('CORRUPTION',corruption)
 assert corruption['local']==0 and 'SHA-256' in corruption['text'],corruption
 # Crash-recovery simulation: object exists but metadata POST was interrupted.
 page.evaluate("""() => {window.mockSongs=[{id:'orphan-safe',title:'Orphan retry',genre:'Pop',created:1,audio:new Blob([new Uint8Array(9000)],{type:'audio/wav'})}];const u='11111111-1111-4111-8111-111111111111';window.mockBlobs[u+'/orphan-safe']=window.mockSongs[0].audio;}""")
 page.locator('[data-nova-sync="push"]').click();page.wait_for_timeout(360)
 healed=page.evaluate('({found:mockCloud.some(x=>x.song_id==="orphan-safe"),text:document.getElementById("nova-cloud-feedback").innerText})')
 print('ORPHAN RECOVERY',healed)
 assert healed['found'] and '1 новых' in healed['text'],healed
 # A conflicting file must NEVER be silently replaced or bound to wrong metadata.
 page.evaluate("""() => {window.mockSongs=[{id:'orphan-conflict',title:'Conflicting orphan',genre:'Pop',created:1,audio:new Blob([new Uint8Array(9000)],{type:'audio/wav'})}];const u='11111111-1111-4111-8111-111111111111';window.mockBlobs[u+'/orphan-conflict']=new Blob([new Uint8Array(9100)],{type:'audio/wav'});}""")
 page.locator('[data-nova-sync="push"]').click();page.wait_for_timeout(360)
 conflict=page.evaluate('({found:mockCloud.some(x=>x.song_id==="orphan-conflict"),text:document.getElementById("nova-cloud-feedback").innerText})')
 print('ORPHAN CONFLICT',conflict)
 assert not conflict['found'] and 'Конфликт аудио' in conflict['text'],conflict
 assert not failures,failures
 browser.close()
print('MOCK E2E PASS: auth → push → dedup → pull; no live HTTP calls')
