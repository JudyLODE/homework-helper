from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t==='10000 以內的數');S.s=i;S.v='sec';render()})()")
    pg.screenshot(path='shots/m1_menu.png',full_page=True)
    print(pg.inner_text('#app')[:200])
