from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t&&x.t.startsWith('綜合練習版面示範'));S.s=i;S.v='sec';render()})()")
    pg.screenshot(path='shots/z_lesson.png',full_page=True)
    print(pg.inner_text('#app')[:700])
    # 進階篇
    pg.click('[data-a=p_go][data-v=z1]')
    for _ in range(6): pg.click('[data-a=p_next]')
    print('---LINK',pg.inner_text('#app')[:300])
    # connect: left0->right with text 海
    def right(t): return pg.locator('.lkb.r',has_text=t).first
    for i,t in enumerate(['海','明','林','好']):
        pg.locator('.lkb:not(.r)').nth(i).click(); right(t).click()
    pg.screenshot(path='shots/z_link.png',full_page=True)
    pg.click('[data-a=p_ck]');print('---CK',pg.inner_text('#app')[-260:]);pg.screenshot(path='shots/z_link_ck.png',full_page=True)
    # basic: fill + rad2
    pg.click('[data-a=paperhome]');print('back',pg.evaluate('S.v'))
    pg.click('[data-a=p_go][data-v=z0]')
    pg.click('[data-a=p_next]');pg.click('[data-a=p_next]')
    pg.screenshot(path='shots/z_fill.png',full_page=True)
    pg.click('[data-a=p_next]');pg.screenshot(path='shots/z_rad2.png',full_page=True)
    pg.click('[data-a=p_next]');pg.screenshot(path='shots/z_tfx.png',full_page=True)
    pg.click('[data-a=paperhome]');pg.click('[data-a=p_go][data-v=z2]');pg.screenshot(path='shots/z_pic.png',full_page=True)
    print(errs)
