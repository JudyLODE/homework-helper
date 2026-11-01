from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    for f in ['cn','math','en','sci','soc']:
        pg.evaluate("f=>{S.v='home';S.f=f;render()}",f);t=pg.inner_text('#app');print(f,len(t),'課程目錄' in t,'上傳這一' in t,'均一' in t,'第一單元' in t)
    print(pg.inner_text('#app')[:300])
    # backup/restore
    pg.evaluate("""()=>{const l={date:iso(),sub:'cn',lang:'zh',t:'第一課 測試',en:'x',pg:'',ic:'📝',c:SUB.cn.c,w:[],d:[],tf:[],calc:[],so:[],mt:[],parent:[],info:null,custom:1,m:['paper'],pp:{title:'t',o:[],h:[],q:[],z:[{t:'基礎篇',secs:[]}],zp:1,map:1}};SEC.push(l);LS.push(l);saveLS();S.v='settings';render()}""")
    pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)");pg.click('[data-a=bk_out]',timeout=3000);txt=pg.input_value('#bkt');print(len(txt),json.loads(txt)['lessons'][0]['t'])
    pg.evaluate("()=>{LS=[];SEC.length=SEC0.length;saveLS()}")
    pg.fill('#bkt',txt);pg.click('[data-a=bk_in]');print(pg.inner_text('#bks'),pg.evaluate("LS.length"))
    pg.click('[data-a=bk_in]');print(pg.inner_text('#bks'),pg.evaluate("LS.length"))
    pg.evaluate("S.v='home';S.f='cn';render()");print('第一課 測試' in pg.inner_text('#app'))
    print(errs)
