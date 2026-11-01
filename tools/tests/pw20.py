import json,base64,io
from playwright.sync_api import sync_playwright
from PIL import Image
imgs=[]
for i in range(40):
    im=Image.new('RGB',(900,1200),(255,255,255));b=io.BytesIO();im.save(b,'JPEG');open(f'/tmp/pg{i}.jpg','wb').write(b.getvalue())
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""
window.__calls=[];
window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:5}}),json:async(pr,o)=>{window.__calls.push((o&&o.images||[]).length);
 const k=window.__calls.length;if(k===5)throw 'busy';
 return [{t:'第'+['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四'][(k-1)%14]+'課 測試',sub:'cn',lang:'zh',w:[['字'+k,'詞'+k,'ㄗ']],d:[],tf:[],info:{h:'x',r:[['課文'+k,'大意']]},parent:[]}]}})};
""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    print(pg.evaluate("typeof SMP"))
    pg.click('[data-a="add"]');pg.click('[data-a="asub"][data-f="cn"]');pg.click('[data-a="amat"][data-f="book"]')
    pg.set_input_files('#ph',[f'/tmp/pg{i}.jpg' for i in range(40)]);pg.wait_for_timeout(1500)
    print('PF',pg.evaluate("PF.length"))
    pg.click("[data-a=ai]")
    pg.wait_for_timeout(45000)
    print(pg.evaluate("window.__calls"));print(pg.evaluate("S.note"));print([s.t for s in []]) if 0 else print(pg.evaluate("SEC.filter(s=>s.custom).map(s=>s.t+':'+s.w.length)"));print(errs)
