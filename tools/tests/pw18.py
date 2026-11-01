from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a=toc]');pg.wait_for_timeout(200)
    print(pg.inner_text('#app')[:500])
    pg.click('[data-a=\"tr\"][data-v=\"2\"]');pg.click('[data-a=\"tr\"][data-v=\"4\"]')
    pg.screenshot(path='shots/toc_cn.png',full_page=True)
    print([x for x in pg.inner_text('#app').split('\n') if '開啟' in x])
    pg.click('[data-a=tk][data-f=en]');print(pg.inner_text('#app')[:420])
    pg.click('[data-a=tk][data-f=cn]');pg.click('[data-a=tgo] >> nth=1');pg.wait_for_timeout(200);print(pg.inner_text('h2'))
    pg.click('[data-a=home]') if pg.query_selector('[data-a=home]') else 0
    pg.click('[data-a=toc]');pg.click('[data-a=tup] >> nth=6');pg.wait_for_timeout(200)
    print(pg.input_value('#lt'),'|',pg.inner_text('.fb.good')[:60])
    pg.reload();pg.click('[data-a=toc]');print(pg.inner_text('.set ul'))
    print(errs)
