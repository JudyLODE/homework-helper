from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    print('toc btn',pg.query_selector('[data-a=toc]') is not None)
    for k in ['cn','math','en','sci','soc']:
        pg.click(f'[data-a="flt"][data-f="{k}"]')
        tx=pg.inner_text('#app')
        print(k,[l for l in tx.split('\n') if '/' in l and ('課程目錄' in l or '學校課程' in l)])
        un=pg.evaluate("SEC.filter(s=>!s.del&&sk(s)==='%s').filter(s=>outIdx('%s',s)<0&&(%s)).map(s=>s.t)"%(k,k,"true" if k!='en' else "ctxOf(s)==='school'"))
        print('  unmatched',un)
    pg.click('[data-a="flt"][data-f="cn"]');pg.click('[data-a=tup] >> nth=5');print(pg.input_value('#lt'),pg.evaluate("S.asub"))
    pg.click('[data-a=home]');pg.click('[data-a="flt"][data-f="en"]');pg.click('[data-a=tup] >> nth=0');print(pg.input_value('#lt'),pg.evaluate("[S.asub,S.actx]"))
    pg.screenshot(path='shots/add_en.png')
    print(errs)
