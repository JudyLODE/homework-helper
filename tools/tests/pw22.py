import io
from playwright.sync_api import sync_playwright
from PIL import Image
Image.new('RGB',(600,800),(255,255,255)).save('/tmp/a1.jpg');Image.new('RGB',(600,800),(250,250,250)).save('/tmp/a2.jpg')
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("""
window.__n=0;window.claude={use:async(n)=>({limits:async()=>({images:{maxCount:1}}),json:async(pr,o)=>{const k=++window.__n;
 return [{t:'第七課 淡水小鎮',sub:'cn',lang:'zh',w:[['字'+k,'詞'+k,'ㄗ']],d:[],tf:[],info:{h:'x',r:[['課文'+k,'大意']]},full:{h:'淡水小鎮',p:k===1?['第一段：淡水是個□美的小鎮。','第二段：河邊很熱鬧。']:['第二段：河邊很熱鬧。','第三段：夕陽很美。']},parent:[]}]}})};
""")
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(800)
    pg.click('[data-a="add"]');pg.click('[data-a="asub"][data-f="cn"]');pg.click('[data-a="amat"][data-f="book"]')
    pg.set_input_files('#ph',['/tmp/a1.jpg','/tmp/a2.jpg']);pg.wait_for_timeout(500);pg.click('[data-a=ai]');pg.wait_for_timeout(8000)
    print(pg.evaluate("S.v"),pg.evaluate("SEC.filter(s=>s.custom).map(s=>[s.t,s.m.join(),s.full&&s.full.p.length])"))
    pg.click('[data-a="mode"][data-m="full"]');print(pg.inner_text('#app')[:300])
    pg.click('[data-a=fedit]');pg.fill('#fx','改一\n\n改二');pg.click('[data-a=fsave]');print(pg.inner_text('#app')[:120])
    pg.reload();print(pg.evaluate("JSON.parse(localStorage.getItem('english-park-lessons'))[0].full.p"))
    print(errs)
