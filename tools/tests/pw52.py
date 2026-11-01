from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t==='10000 以內的數');S.s=i;S.v='sec';render()})()")
    for zi in range(5):
        pg.evaluate("(zi)=>{ppStart('z'+zi)}",zi)
        n=pg.evaluate("ppSecs().length")
        for si in range(n):
            pg.evaluate("(si)=>{S.pp.i=si;render()}",si)
            pg.screenshot(path=f'shots/n_{zi}_{si}.png',full_page=True)
