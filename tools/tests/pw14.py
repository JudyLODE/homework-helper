import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':430,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1200)
        await pg.evaluate("""()=>{
          const base=PPD.c3;
          SMP={limits:async()=>({images:{maxCount:8}}),json:async(prompt,opts)=>{
            if(prompt.includes('原卷：'))return {lessons:[{title:'h',secs:JSON.parse(JSON.stringify(base.h))}]};
            if(prompt.includes('本課專屬'))return {lessons:[{title:'本課單元測驗卷',secs:JSON.parse(JSON.stringify(base.o))}]};
            return {lessons:[]}}};
          // 第三課綜合練習(無paper) -> 設計
          S.s=SEC.findIndex(s=>s.t.startsWith('第三課 綜合'));S.v='sec';render();}""")
        print('design btn:',await pg.locator('[data-a="p_design"]').count())
        await pg.click('[data-a="p_design"]')
        await pg.wait_for_function("SEC[S.s].pp",timeout=30000)
        print(await pg.evaluate("[S.s,SEC[S.s].t,SEC[S.s].custom,SEC[S.s].m.join(),SEC[S.s].pp.o.length,SEC[S.s].pp.h.length,S.note]"))
        await pg.screenshot(path='/home/claude/shots/pp_designed.png',full_page=True)
        # open paper home and press 再出加深版
        await pg.click('[data-a="mode"][data-m="paper"]')
        await pg.screenshot(path='/home/claude/shots/pp_home2.png',full_page=True)
        await pg.click('[data-a="p_hard"]')
        await pg.wait_for_timeout(1500)
        print(await pg.evaluate("[S.v,SEC[S.s].pp.h.length,S.note]"))
        # reload persistence
        await pg.reload();await pg.wait_for_timeout(1000)
        print('persist',await pg.evaluate("SEC.filter(s=>s.pp).map(s=>[s.t,s.pp.o.length,(s.pp.h||[]).length])"))
        print(errs)
        await b.close()
asyncio.run(main())
