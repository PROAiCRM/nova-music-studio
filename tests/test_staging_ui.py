from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text()
checks=0
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for w,h in [(375,812),(390,844),(430,932),(768,1024),(1024,768),(1440,900)]:
      for theme in ('light','graphite'):
        page=browser.new_page(viewport={'width':w,'height':h})
        errors=[];requests=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.on('request', lambda r: requests.append(r.url) if 'hgvxvcljlwclbucaoicl.supabase.co' in r.url else None)
        page.set_content(html,wait_until='domcontentloaded',timeout=15000)
        page.evaluate('(t)=>{window.NOVA_THEME?.setTheme?.(t);document.documentElement.dataset.numeraTheme=t}',theme)
        for route in ('home','create','library','studio'):
          page.evaluate('(v)=>{location.hash="#"+v}',route)
          page.wait_for_timeout(60)
          assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+2'), (w,theme,route,'overflow')
          assert page.evaluate('NOVA_SYNC_STATUS().configured'),(w,theme,route,'cloud not configured')
          assert not errors,(w,theme,route,errors)
          checks+=1
        assert requests==[],('Unexpected background Supabase request',requests)
        if w==390:
          page.evaluate('location.hash="#studio"')
          page.wait_for_timeout(70)
          assert page.locator('#nova-cloud-block').count()==1
          assert page.locator('#nova-cloud-auth').is_visible()
          assert not page.locator('#nova-cloud-controls').is_visible()
          page.screenshot(path=str(root/('preview_%s.png'%theme)),full_page=True)
        page.close()
    browser.close()
print(f'UI / no-background-network PASS {checks}/48')
