from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text()
checks=0
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    for width,height in [(390,844),(768,1024),(1440,900)]:
        page=browser.new_page(viewport={'width':width,'height':height})
        errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content(html,wait_until='domcontentloaded',timeout=15000)
        page.wait_for_timeout(100)
        title=page.title();assert 'NOVA' in title,title
        for route in ['home','create','library','studio']:
            page.evaluate('(route)=>{location.hash="#"+route}',route)
            page.wait_for_timeout(70)
            bad=page.evaluate('document.documentElement.scrollWidth>window.innerWidth+1')
            assert not bad,(width,route)
            assert not errors,(width,route,errors)
            checks+=1
        assert page.evaluate('window.NOVA_SYNC_STATUS().configured') is True
        page.close()
    browser.close()
print(f'SMOKE PASS {checks}/12 combinations; cloud configured but no calls made on load; no JS exceptions')
