from playwright.sync_api import sync_playwright
from PIL import Image
Image.new('RGB',(600,800),(255,255,255)).save('/tmp/a1.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""window.__pr=[];window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:5}}),json:async(pr,o)=>{
 if(pr.includes('請依這些內容設計')){window.__pr.push(pr.includes('照樣寫句'));return {lessons:[{title:'測驗題',secs:[
  {k:'zy',g:'生字',t:'測驗：生字',pt:1,items:[{c:'絲',w:'絲帶',o:['ㄕ','ㄙ','ㄒㄧˊ'],a:1}]},
  {k:'sent',g:'句型',t:'測驗：句型',pt:2,items:[{kw:'一邊…一邊…',ref:'我一邊走路一邊唱歌。'}]}]}]}}
 return {lessons:[{title:'字的小旅行',secs:[
 {k:'txt',g:'',t:'課文',pt:1,items:[{p:'第一段。'}]},
 {k:'tbl',g:'',t:'生字',pt:1,head:['字','注音'],items:[{c:['絲','ㄙ']}]},
 {k:'txt',g:'',t:'句型重點',pt:1,items:[{p:'一邊…一邊…'}]}]}]}}})};""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="flt"][data-f="cn"]')
    pg.locator('[data-a=tup][data-t="第一課 字的小旅行"]').click()
    pg.set_input_files('#ph','/tmp/a1.jpg');pg.wait_for_timeout(400);pg.click('[data-a=ai]');pg.wait_for_timeout(6000)
    print(pg.evaluate("[S.v,window.__pr,SEC.filter(s=>s.custom).map(s=>[s.t,s.pp.o.length,(s.pp.q||[]).length])]"))
    print(pg.inner_text('#app')[:500])
    pg.click('[data-a=back][data-v=home], .back >> nth=0') if False else None
    print(errs)
