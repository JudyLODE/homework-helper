from playwright.sync_api import sync_playwright
from PIL import Image
Image.new('RGB',(600,800),(255,255,255)).save('/tmp/a1.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:3}}),json:async(pr,o)=>[{t:'學習地圖一 整理',sub:'cn',lang:'zh',w:[['字','詞','ㄗ']],d:[],tf:[],info:{h:'x',r:[['重點','說明']]},parent:[]}]})};""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="flt"][data-f="cn"]')
    btn=pg.locator('[data-a=tup][data-t="學習地圖一"]');print(btn.count(),btn.inner_text())
    btn.click();print(pg.input_value('#lt'),pg.evaluate("[S.asub,S.amat]"))
    pg.set_input_files('#ph','/tmp/a1.jpg');pg.wait_for_timeout(400);pg.click('[data-a=ai]');pg.wait_for_timeout(4000)
    print(pg.evaluate("SEC.filter(s=>s.custom).map(s=>s.t)"))
    pg.click('[data-a=home]');pg.click('[data-a="flt"][data-f="cn"]')
    print([l for l in pg.inner_text('#app').split('\n') if '學習地圖一' in l]);print(errs)
