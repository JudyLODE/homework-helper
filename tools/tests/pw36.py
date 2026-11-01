from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    def chk(tag):
        h=pg.inner_html('#app');print(tag,'🔊' in h,pg.locator('.spd').count(),pg.locator('.say').count())
    chk('home')
    pg.click('[data-a=settings]');chk('settings');pg.click('[data-a=home]')
    res=pg.evaluate("""(()=>{const o={};SEC.forEach((s,i)=>{if(s.del)return;const k=sk(s);if(!o[k])o[k]=[]; if(o[k].length<2)o[k].push(i)});return o})()""")
    print(res)
    for k,ids in res.items():
        for i in ids:
            pg.evaluate(f"S.s={i};S.v='sec';render()");
            modes=pg.evaluate("SEC[S.s].m")
            for m in modes:
                try:
                    pg.evaluate(f"S.s={i};S.v='sec';render()")
                    pg.click(f'[data-a=mode][data-m={m}]',timeout=1500)
                except Exception as e: continue
                pg.wait_for_timeout(80)
                h=pg.inner_html('#app')
                print(k,i,m,'🔊' in h,pg.locator('.spd').count(),pg.locator('.say').count())
    print(errs)
