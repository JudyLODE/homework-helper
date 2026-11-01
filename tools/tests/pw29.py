from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(500)
    mk="""(t)=>{const s={date:iso(),sub:'cn',lang:'zh',custom:1,t:t,en:'x',pg:'',ic:'📖',c:SUB.cn.c,m:['cards'],w:[['字','詞','']],d:[],tf:[],calc:[],so:[],mt:[],parent:[]};LS.push(s);SEC.push(s)}"""
    pg.evaluate("(%s)('第四課 小丑魚和海葵');(%s)('第七課 淡水小鎮');(%s)('第五課 習作：綜合練習')"%(mk,mk,mk))
    pg.click('[data-a="flt"][data-f="cn"]')
    print([l for l in pg.inner_text('#app').split('\n') if l.startswith('第') or l.startswith('學習') or l.startswith('閱讀')][:30]);print(errs)
