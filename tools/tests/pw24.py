from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    print(pg.evaluate("SEC.filter(s=>s.sub==='math').map(s=>[s.t,s.en,s.m.join(),s.d.length,s.calc.length])"))
    print('翰林' in pg.evaluate("JSON.stringify(SEC.filter(s=>s.sub==='math'))"))
    pg.click('[data-a=toc]');pg.click('[data-a=tk][data-f=math]');print(pg.inner_text('#app')[220:420]);print(errs)
