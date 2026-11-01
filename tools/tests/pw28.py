from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(500)
    pg.evaluate("localStorage.removeItem('hw-wipe35');LS.push({date:iso(),sub:'cn',lang:'zh',custom:1,t:'第三課 繞口令村',en:'',pg:'',ic:'📖',c:SUB.cn.c,m:['cards'],w:[['字','詞','']],d:[],tf:[],calc:[],so:[],mt:[],parent:[]},{date:iso(),sub:'cn',lang:'zh',custom:1,t:'第二課 妙故事點點名',en:'',pg:'',ic:'📖',c:SUB.cn.c,m:['cards'],w:[['字','詞','']],d:[],tf:[],calc:[],so:[],mt:[],parent:[]});saveLS()")
    pg.reload();pg.wait_for_timeout(500)
    print([x for x in pg.inner_text('.chips2').split('\n')])
    pg.click('[data-a="flt"][data-f="cn"]')
    print(pg.evaluate("document.querySelectorAll('button[data-a=sec]').length"),pg.evaluate("[...document.querySelectorAll('button[data-a=sec] b')].map(b=>b.textContent)"))
    print([l for l in pg.inner_text('#app').split('\n') if '課程目錄' in l])
    print(errs)
