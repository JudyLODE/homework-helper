from playwright.sync_api import sync_playwright
from PIL import Image
Image.new('RGB',(600,800),(255,255,255)).save('/tmp/a1.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""window.__pr=[];window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:5}}),json:async(pr,o)=>{
 if(pr.includes('請依這些內容設計')){window.__pr.push('quiz');return {lessons:[{title:'測驗題',secs:[
  {k:'mc',g:'一、認識敘述四要素：人、時、地、事',t:'測驗：敘事四要素',pt:2,items:[{q:'「小明昨天在公園放風箏」，哪一個是「地」？',o:['小明','昨天','公園'],a:2,why:'公園是地點'}]},
  {k:'ord',g:'二、閱讀有方法',t:'測驗：詞語重組',pt:2,items:[{w:['我','愛','讀書']}]}]}]}}
 window.__pr.push('map');return {title:'學習地圖一',secs:[
 {k:'tbl',g:'一、認識敘述四要素：人、時、地、事',t:'敘事四要素',d:'',pt:1,head:['要素','說明'],items:[{c:['人','誰']},{c:['時','什麼時候']}]},
 {k:'txt',g:'一、認識敘述四要素：人、時、地、事',t:'認識敘述四要素：人、時、地、事',d:'',pt:1,items:[{p:'範例文字。'}]},
 {k:'txt',g:'二、閱讀有方法',t:'（一）拆字造詞',d:'',pt:1,items:[{p:'第一段文字。'},{p:'第二段文字。'}]}]}}})};""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="flt"][data-f="cn"]')
    pg.locator('[data-a=tup][data-t="學習地圖一"]').click()
    pg.set_input_files('#ph','/tmp/a1.jpg');pg.wait_for_timeout(400);pg.click('[data-a=ai]');pg.wait_for_timeout(6000)
    print(pg.evaluate("[S.v,window.__pr,SEC.filter(s=>s.custom).map(s=>[s.t,s.pp.o.length,(s.pp.q||[]).length])]"))
    print(pg.inner_text('#app')[:900]);pg.screenshot(path='shots/map4.png',full_page=True)
    pg.locator('details.mc summary').first.click();print('OPEN',pg.locator('details.mc[open]').count())
    pg.click('[data-a=p_go][data-v=o]');print('---Q1',pg.inner_text('#app')[:300])
    pg.click('[data-a=p_circ], .pc.l >> nth=0') if False else None
    pg.click('[data-a=p_next]');print('---Q2',pg.inner_text('#app')[:200])
    pg.click('[data-a=paperhome]');print('---BACK',pg.evaluate("S.v"))
    pg.click('[data-a=p_quiz]');pg.wait_for_timeout(3000);print(pg.evaluate("[window.__pr,S.v]"),pg.inner_text('#app')[:120])
    print(errs)
