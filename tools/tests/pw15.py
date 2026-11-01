import asyncio,json
from playwright.async_api import async_playwright
FILL="""([i,ver])=>{
  S.s=i;S.v='sec';render();
  document.querySelector('[data-a="mode"][data-m="paper"]').click();
  ppStart(ver);
  const secs=ppSecs();const A=S.pp.a;
  secs.forEach((sec,si)=>sec.items.forEach((it,ii)=>{const k=si+'.'+ii;
    switch(sec.k){
     case 'write':wparse(it.s).filter(x=>x.m).forEach((x,j)=>A[k+'.'+j]=it.a[j]);break;
     case 'zy':case 'mc':case 'cls':A[k]=it.a;break;
     case 'tfx':A[k]=it.a?1:0;break;
     case 'fix':A[k+'.c']=fixPos(it.s,it.w);[...it.a].forEach((c,j)=>A[k+'.t'+j]=c);break;
     case 'bank':it.a.forEach((c,j)=>A[k+'.'+j]=c);break;
     case 'ordc':it.a.forEach((c,j)=>A[k+'.'+j]=String(c));break;
     case 'pick':it.a.forEach((v,j)=>A[k+'.'+j]=v);break;
     case 'rad':A[k+'.r']=radRef(it.c,it);A[k+'.w']=it.ws[0];break;
     case 'verb':{const tk=it.s.split('|');A[k]=tk.map((t,j)=>it.a.includes(t)?j:-1).filter(j=>j>=0);break}
     case 'ord':A[k]=it.w.map((_,j)=>j);break;
     case 'like':{const n=(it.tpl.match(blankRe)||[]).length;for(let j=0;j<n;j++){A[k+'.'+j]='字';S.pp.pc[k+'.'+j]=1}break}
     case 'sent':A[k]='只要努力就會成功';S.pp.pc[k]=1;break;
    }}));
  const T=ppTotal();return {ver,got:T.got,max:T.max,rows:T.rows.map(r=>r.got+'/'+r.max).join(' ')}
}"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':430,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1500)
        idxs=await pg.evaluate('SEC.map((s,i)=>s.pp?[i,s.t,s.pp.o.length,(s.pp.h||[]).length]:null).filter(Boolean)')
        for (i,t,no,nh) in idxs:
            for ver in ('o','h'):
                print(t,ver,await pg.evaluate(FILL,[i,ver]))
        print('modes',await pg.evaluate("SEC.map(s=>[s.t,s.m.join()])"))
        # real UI: 習作基礎
        i=[x[0] for x in idxs if '基礎' in x[1]][0]
        await pg.evaluate(FILL,[i,'o'])
        await pg.evaluate("S.pp=null;render()")
        await pg.click('[data-a="p_go"][data-v="o"]')
        # sec1 write: type zhuyin
        ins=pg.locator('input.pi');n=await ins.count();print('inputs',n)
        await ins.nth(0).fill('努');await ins.nth(1).fill('練');await ins.nth(2).fill('ㄨˇ');await ins.nth(3).fill('ㄉㄢ')
        await pg.screenshot(path='/home/claude/shots/c5b_1.png',full_page=True)
        await pg.click('[data-a="p_ck"]');print('s1',await pg.inner_text('.secsc'))
        await pg.screenshot(path='/home/claude/shots/c5b_1c.png',full_page=True)
        for si in range(2,8):
            await pg.click('[data-a="p_next"]');await pg.screenshot(path=f'/home/claude/shots/c5b_{si}.png',full_page=True)
        print('title',await pg.inner_text('.pt'))
        # ordc typing
        ins=pg.locator('input.pi')
        for q,v in enumerate('3124'): await ins.nth(q).fill(v)
        await pg.click('[data-a="p_ck"]');print('ordc',await pg.inner_text('.secsc'))
        # 進階 bank
        i=[x[0] for x in idxs if '進階' in x[1]][0]
        await pg.evaluate("([i])=>{S.pp=null;S.s=i;S.v='sec';render();document.querySelector('[data-a=\"mode\"][data-m=\"paper\"]').click()}",[i])
        await pg.click('[data-a="p_go"][data-v="o"]')
        for _ in range(1): await pg.click('[data-a="p_next"]')
        await pg.screenshot(path='/home/claude/shots/c5a_2.png',full_page=True)
        await pg.click('[data-a="p_circ"][data-k="1.0"][data-v="9"]')
        await pg.screenshot(path='/home/claude/shots/c5a_2b.png',full_page=True)
        await pg.click('[data-a="p_next"]');await pg.screenshot(path='/home/claude/shots/c5a_3.png',full_page=True)
        await pg.click('[data-a="p_next"]');await pg.click('[data-a="p_next"]');await pg.click('[data-a="p_next"]')
        await pg.screenshot(path='/home/claude/shots/c5a_6.png',full_page=True)
        print('errs',errs)
        await b.close()
asyncio.run(main())
