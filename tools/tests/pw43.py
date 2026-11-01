from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t&&x.t.startsWith('數學習作版面示範'));S.s=i;S.v='sec';render()})()")
    pg.click('[data-a=p_go][data-v=z0]')
    for i in range(9):
        pg.evaluate("i=>{S.pp.i=i;render()}",i)
        n=pg.locator('[data-a=p_rg]').count()
        if n: pg.click('[data-a=p_rg]')
        print(i,n,pg.evaluate("ppSecs()[%d].k"%i),errs[-1:] )
