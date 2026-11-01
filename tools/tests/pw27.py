from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(500)
    pg.evaluate("localStorage.setItem('hw-hidecn','1')");pg.reload();pg.click('[data-a="flt"][data-f="cn"]')
    print(pg.evaluate("document.querySelectorAll('button[data-a=sec]').length"))
