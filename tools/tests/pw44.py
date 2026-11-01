from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b=p.chromium.launch();ctx=b.new_context(viewport={'width':430,'height':900},color_scheme='dark');pg=ctx.new_page()
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t&&x.t.startsWith('數學習作版面示範'));S.s=i;S.v='sec';render()})()")
    pg.click('[data-a=p_go][data-v=z0]')
    for i,n in [(0,'a'),(2,'b'),(7,'c'),(8,'d')]:
        pg.evaluate("i=>{S.pp.i=i;render()}",i)
        if i==2: pg.fill('[data-k="2.0.0"]','6000')
        pg.screenshot(path=f'shots/n_{n}.png',full_page=True)
ims=[Image.open(f'/home/claude/shots/n_{n}.png') for n in 'abcd']
h=max(i.size[1] for i in ims);W=sum(i.size[0] for i in ims)
o=Image.new('RGB',(W,h),'white');x=0
for i in ims:o.paste(i,(x,0));x+=i.size[0]
o.save('/home/claude/shots/n_all.png')
