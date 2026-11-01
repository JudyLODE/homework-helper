import asyncio,json,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1217/chrome-linux/chrome') if False else await p.chromium.launch()
        pg=await b.new_page(viewport={'width':430,'height':900})
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.on('console',lambda m:errs.append('C:'+m.text) if m.type=='error' else None)
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html')
        await pg.wait_for_timeout(1500)
        print('dict',await pg.evaluate('!!DICT && Object.keys(DICT.ch).length+" chars, "+DICT.ws.size+" words"'))
        idxs=await pg.evaluate('SEC.map((s,i)=>s.pp?[i,s.t,s.pp.o.length,(s.pp.h||[]).length]:null).filter(Boolean)')
        print(idxs)
        for (i,t,no,nh) in idxs:
            for ver in ('o','h'):
                r=await pg.evaluate('''([i,ver])=>{
                  S.s=i;S.v='sec';render();
                  document.querySelector('[data-a="mode"][data-m="paper"]').click();
                  ppStart(ver);
                  const secs=ppSecs();const A=S.pp.a;
                  secs.forEach((sec,si)=>sec.items.forEach((it,ii)=>{const k=si+'.'+ii;
                    switch(sec.k){
                     case 'write':A[k]=it.a;break;
                     case 'zy':case 'mc':case 'cls':A[k]=it.a;break;
                     case 'tfx':A[k]=it.a?1:0;break;
                     case 'fix':A[k+'.w']=it.s.indexOf(it.w);A[k+'.t']=it.a;break;
                     case 'pick':it.a.forEach((v,j)=>A[k+'.'+j]=v);break;
                     case 'rad':A[k+'.r']=radRef(it.c,it);A[k+'.w']=it.ws[0];break;
                     case 'verb':{const tk=it.s.split('|');A[k]=tk.map((t,j)=>it.a.includes(t)?j:-1).filter(j=>j>=0);break}
                     case 'ord':A[k]=it.w.map((_,j)=>j);break;
                     case 'like':{const n=(it.tpl.match(blankRe)||[]).length;for(let j=0;j<n;j++){A[k+'.'+j]='字';S.pp.pc[k+'.'+j]=1}break}
                     case 'sent':A[k]='只要努力就會成功';S.pp.pc[k]=1;break;
                    }}));
                  const T=ppTotal();return {ver,got:T.got,max:T.max,rows:T.rows.map(r=>r.got+'/'+r.max).join(' ')}
                }''',[i,ver])
                print(t,ver,r)
        # UI walk-through on c5 original: real clicks
        i5=[x[0] for x in idxs if '第五課' in x[1]][0]
        await pg.evaluate('([i])=>{S.s=i;S.v="sec";render();document.querySelector(\'[data-a="mode"][data-m="paper"]\').click();}',[i5])
        await pg.screenshot(path='/home/claude/shots/pp_home.png')
        await pg.click('[data-a="p_go"][data-v="o"]')
        # sec1 write: type
        inputs=pg.locator('input.pi')
        n=await inputs.count();print('write inputs',n)
        await inputs.nth(0).fill('壓');await inputs.nth(1).fill('該');await inputs.nth(2).fill('錯')
        await pg.screenshot(path='/home/claude/shots/pp_s1.png',full_page=True)
        await pg.click('[data-a="p_ck"]')
        print(await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/pp_s1c.png',full_page=True)
        # go through sections with screenshots
        for si in range(2,12):
            await pg.click('[data-a="p_next"]')
            await pg.wait_for_timeout(100)
            await pg.screenshot(path=f'/home/claude/shots/pp_s{si}.png',full_page=True)
        print(await pg.evaluate('S.pp.sum'))
        await pg.click('[data-a="p_next"]')
        await pg.screenshot(path='/home/claude/shots/pp_sum.png',full_page=True)
        print('errs',errs)
        await b.close()
asyncio.run(main())
