import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':430,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1200)
        await pg.evaluate('()=>{S.s=SEC.findIndex(s=>s.ppk==="c5");S.v="sec";render();document.querySelector(\'[data-a="mode"][data-m="paper"]\').click();}')
        await pg.click('[data-a="p_go"][data-v="o"]')
        async def go(n):
            for _ in range(n): await pg.click('[data-a="p_next"]')
        # 三 fix: real clicks
        await go(2)
        await pg.click('[data-a="p_circ"][data-k="2.0"][data-v="2"]')  # 立
        await pg.locator('input.pi').nth(0).fill('利')
        await pg.click('[data-a="p_circ"][data-k="2.1"][data-v="3"]')  # wrong char (力?) deliberately wrong
        await pg.locator('input.pi').nth(1).fill('努')
        await pg.click('[data-a="p_ck"]')
        print('fix',await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/pp_fix.png',full_page=True)
        # 四 pick: wrong then right
        await go(1)
        await pg.click('[data-a="p_ch"][data-k="3.0.0"][data-v="0"]'); await pg.click('[data-a="p_ch"][data-k="3.0.1"][data-v="0"]')
        await pg.click('[data-a="p_ck"]');print('pick',await pg.inner_text('.secsc'))
        # 五 rad: 部首 玉 alt 王; word typed
        await go(1)
        ins=pg.locator('input.pi')
        await ins.nth(0).fill('糸部'); await ins.nth(1).fill('整理')
        await ins.nth(2).fill('殳'); await ins.nth(3).fill('分段')   # 分段 maybe unk
        await ins.nth(4).fill('王'); await ins.nth(5).fill('球')       # bad word (single)
        await pg.click('[data-a="p_ck"]');print('rad',await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/pp_rad.png',full_page=True)
        # 六 verb click
        await go(1)
        await pg.click('[data-a="p_tk"][data-k="5.0"][data-v="6"]')
        await pg.click('[data-a="p_tk"][data-k="5.1"][data-v="0"]')
        await pg.click('[data-a="p_ck"]');print('verb',await pg.inner_text('.secsc'))
        # 十 like + 十一 sent parent confirm
        await go(4)  # 7,8,9,10 -> index 9 (十)
        print('on', await pg.inner_text('.pt'))
        ins=pg.locator('input.pi')
        for i in range(3): await ins.nth(i).fill('畫出最美的圖畫'[i])
        await pg.click('[data-a="p_ck"]')
        print('like before parent',await pg.inner_text('.secsc'))
        await pg.click('[data-a="p_pc"][data-k="9.0.0"][data-v="1"]')
        print('like after parent',await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/pp_like.png',full_page=True)
        await go(1)
        await pg.locator('textarea.pi').fill('只要努力，就會進步。')
        await pg.click('[data-a="p_ck"]')
        await pg.click('[data-a="p_pc"][data-k="10.0"][data-v="1"]')
        print('sent',await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/pp_sent.png',full_page=True)
        # ord on c3
        await pg.evaluate('()=>{S.pp=null;S.s=SEC.findIndex(s=>s.ppk==="c3");S.v="sec";render();document.querySelector(\'[data-a="mode"][data-m="paper"]\').click();}')
        await pg.click('[data-a="p_go"][data-v="o"]')
        await go(7)
        print('on', await pg.inner_text('.pt'))
        w=await pg.evaluate('ppSecs()[7].items[0].w')
        for ww in w:
            # click pool button with this text
            await pg.locator('.ordp .pc',has_text=ww).first.click()
        await pg.click('[data-a="p_ck"]');print('ord',await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/pp_ord.png',full_page=True)
        print('errs',errs)
        await b.close()
asyncio.run(main())
