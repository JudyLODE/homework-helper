from playwright.sync_api import sync_playwright
from PIL import Image
Image.new('RGB',(600,800),(255,255,255)).save('/tmp/a1.jpg');Image.new('RGB',(600,800),(250,250,250)).save('/tmp/a2.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""
window.__n=0;window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:1}}),json:async(pr,o)=>{const k=++window.__n;
 return [{t:'第七課 淡水小鎮',sub:'cn',lang:'zh',w:[['字'+k,'詞'+k,'ㄗ']],d:[],tf:[],info:{h:'x',r:[['課文'+k,'大意']]},full:{h:'測試課文',p:k===1?['甲段□。','乙段。']:['乙段。','丙段。']},parent:[]}]}})};
""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="add"]');pg.click('[data-a="asub"][data-f="cn"]');pg.click('[data-a="amat"][data-f="book"]')
    pg.set_input_files('#ph',['/tmp/a1.jpg','/tmp/a2.jpg']);pg.wait_for_timeout(500);pg.click('[data-a=ai]');pg.wait_for_timeout(8000)
    print(pg.evaluate("S.v"),pg.evaluate("SEC.filter(s=>s.custom).map(s=>[s.t,s.m.join(),!!s.full])"))
    pg.click('[data-a=home]');pg.click('[data-a=ft]');print(pg.inner_text('#app')[:200]);
    print(pg.evaluate("JSON.stringify(FT)"))
    pg.click('summary >> text=第一課');pg.click('[data-a=fedit][data-k="第一課"]');pg.fill('#fx','手動甲\n\n手動乙');pg.click('[data-a=fsave]')
    pg.reload();pg.click('[data-a=ft]');print(pg.evaluate("Object.keys(FT)"))
    pg.click('[data-a=home]');pg.click('[data-a=toc]');print([x for x in pg.inner_text('#app').split('\n') if '課文全文' in x][:4])
    print(errs)
