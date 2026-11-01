from playwright.sync_api import sync_playwright
from PIL import Image
Image.new('RGB',(600,800),(255,255,255)).save('/tmp/a1.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""window.__pr=[];window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:5}}),json:async(pr,o)=>{window.__pr.push(pr.includes('學習地圖'));return {result:{pages:[{title:'學習地圖一',secs:[
 {k:'tbl',g:'一、測試大單元一',t:'內容甲',d:'',pt:1,head:['要素','說明'],items:[{c:['人','誰']},{c:['時','什麼時候']}]},
 {k:'mc',g:'一、測試大單元一',t:'練習乙',d:'選一選',pt:2,items:[{q:'題目？',o:['甲','乙','丙'],a:1,why:'因為'}]},
 {k:'txt',g:'二、測試大單元二',t:'（一）',d:'',pt:1,items:[{p:'第一段文字。'},{p:'第二段文字。'}]},
 {k:'tfx',g:'二、測試大單元二',t:'（二）',d:'',pt:1,items:[{s:'敘述',a:true,why:'理由'}]}]}]}}}})};""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="flt"][data-f="cn"]')
    pg.locator('[data-a=tup][data-t="學習地圖一"]').click();print(pg.evaluate("S.amat"))
    pg.set_input_files('#ph','/tmp/a1.jpg');pg.wait_for_timeout(400);pg.click('[data-a=ai]');pg.wait_for_timeout(5000)
    print(pg.evaluate("[S.v,window.__pr,SEC.filter(s=>s.custom).map(s=>[s.t,s.m.join(),s.pp.map,s.pp.h.length])]"))
    print(pg.inner_text('#app')[:300])
    pg.click('[data-a=mode][data-m=paper]');print(pg.inner_text('#app')[:500])
    pg.click('[data-a=p_go][data-v=o]');print('---P1',pg.inner_text('#app')[:400])
    pg.click('[data-a=p_next]');print('---P2',pg.inner_text('#app')[:300])
    pg.click('[data-a=p_next]');print('---P3',pg.inner_text('#app')[:300]);pg.screenshot(path='shots/map3.png')
    pg.click('[data-a=p_next]');pg.click('[data-a=p_next]');print('---SUM',pg.inner_text('#app')[:300]);print(errs)
