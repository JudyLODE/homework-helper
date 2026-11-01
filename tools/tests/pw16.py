import asyncio,json
from playwright.async_api import async_playwright
IM1='/mnt/user-data/attachments/d7dced68-e677-552b-8070-720d7f141e4d/79723fe4-image.jpg'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':430,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1200)
        await pg.evaluate("""()=>{
          SMP={limits:async()=>({images:{maxCount:8}}),json:async(prompt,opts)=>{
            if(prompt.includes('原卷：')){const o=JSON.parse(prompt.split('原卷：')[1]);const src=Object.values(PPD).find(p=>p.o.length===o.secs.length&&p.o[0].k===o.secs[0].k&&p.title===o.title);const h=Object.values(PPD).find(p=>p.title===o.title).h;return {lessons:[{title:o.title,secs:h}]}}
            return {lessons:[{sub:'cn',title:PPD.c5b.title,secs:PPD.c5b.o},{sub:'cn',title:PPD.c5a.title,secs:PPD.c5a.o}]}}};
          S.v='add';S.asub='cn';S.amat='work';render();}""")
        await pg.set_input_files('#ph',[IM1])
        await pg.click('[data-a="ai"]')
        await pg.wait_for_function("S.v==='sec'",timeout=60000)
        print(await pg.evaluate("SEC.filter(s=>s.custom).map(s=>[s.t,s.m.join(),s.pp.o.length,s.pp.h.length])"),await pg.evaluate("S.note"))
        # norm filter
        r=await pg.evaluate("""()=>{const x=norm({sub:'cn',t:'測',w:[['詞','ㄘ｜意','😀'],['詞2','ㄘ｜意','😀'],['詞3','ㄘ｜意','😀']],d:[['「綁」去除部首外，還有幾畫？','','7','x',['5','6']],['「迷」的意思？','','迷路','y',['a','b']]],calc:[['1+1',2,'',[],'']],tf:[['請跟著唸三次。',true,'']]});return x?{d:x.d.length,calc:x.calc.length,tf:x.tf.length,m:x.m}:null}""")
        print('norm',r)
        # cn view: no speed btn, no say
        await pg.evaluate("S.s=SEC.findIndex(s=>s.t==='第五課 飛舞的絲帶');S.v='sec';render()")
        print('spd in sec',await pg.locator('.spd').count())
        await pg.click('[data-a="mode"][data-m="info"]');print('say btns',await pg.locator('.say').count(),'spd',await pg.locator('.spd').count())
        await pg.screenshot(path='/home/claude/shots/cn_info.png',full_page=True)
        await pg.evaluate("S.v='sec';render()");await pg.click('[data-a="mode"][data-m="cards"]');print('cards say',await pg.locator('.say').count())
        await pg.screenshot(path='/home/claude/shots/cn_cards.png')
        await pg.evaluate("S.v='home';render()");print('home spd',await pg.locator('.spd').count())
        print(errs);await b.close()
asyncio.run(main())
