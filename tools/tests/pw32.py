from playwright.sync_api import sync_playwright
from PIL import Image
for i in range(9): Image.new('RGB',(600,800),(255,255,255)).save(f'/tmp/m{i}.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""window.__n=0;window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:4}}),json:async(pr,o)=>{const k=++window.__n;
 if(k===1)return [{title:'第一課 測試課',secs:[{k:'txt',g:'',t:'課文',pt:1,items:[{p:'甲段'}]},{k:'tbl',g:'',t:'生字',pt:1,head:['字','詞'],items:[{c:['甲','甲乙']}]}]}];
 if(k===2)return [{title:'第一課 測試課',secs:[{k:'txt',g:'',t:'課文',pt:1,items:[{p:'甲段'}]},{k:'num',g:'',t:'練習',pt:2,items:[{q:'1+1=？',a:'2'}]}]},{title:'學習地圖一',secs:[{k:'tfx',g:'一、大標',t:'我會運用',pt:1,items:[{s:'敘述',a:true,why:'x'}]}]}];
 return [{title:'第二課',secs:[{k:'txt',g:'',t:'課文',pt:1,items:[{p:'乙段'}]}]}]}})};""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="flt"][data-f="cn"]')
    pg.locator('[data-a=tup]').first.click();print(pg.evaluate("[S.asub,S.amat,S.preT]"))
    pg.set_input_files('#ph',[f'/tmp/m{i}.jpg' for i in range(9)]);pg.wait_for_timeout(1500);pg.click('[data-a=ai]');pg.wait_for_timeout(15000)
    print(pg.evaluate("[S.v,window.__n,SEC.filter(s=>s.custom).map(s=>[s.t,s.pp.o.map(z=>z.k+':'+z.t).join('|')])]"))
    print(pg.inner_text('#app')[:300]);print(errs)
