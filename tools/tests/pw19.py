from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    print(pg.inner_text('#app')[:1500]);pg.screenshot(path='shots/home_all.png',full_page=True)
    pg.click('[data-a="flt"][data-f="en"]');print('---EN');print(pg.inner_text('#app')[:900])
    pg.click('[data-a="tkgo"]');print('---',pg.inner_text('h2'))
    pg.click('[data-a="home"]');pg.click('[data-a="add"]');print(pg.inner_text('#app')[:300])
    pg.click('[data-a="actx"][data-f="school"]');print(pg.eval_on_selector_all('#cx .chip','e=>e.map(x=>x.className)'))
    print(errs)
