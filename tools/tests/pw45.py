from playwright.sync_api import sync_playwright
FILL="""si=>{const sec=ppSecs()[si],A=S.pp.a;sec.items.forEach((it,ii)=>{const k=si+'.'+ii;
 if(sec.k==='blk'){it.d.forEach((x,i)=>A[k+'.'+i]=String(x));A[k+'.4']=String(dnum(it.d))}
 if(sec.k==='pv'){[...String(it.n)].forEach((c,i)=>A[k+'.'+i]=c)}
 if(sec.k==='seq'){it.blank.forEach((b,j)=>A[k+'.'+j]=String(it.v[b]))}
 if(sec.k==='cmp')A[k]=it.a;
 if(sec.k==='draw'){let r=it.price;DEN.forEach((v,i)=>{A[k+'.q'+i]=Math.floor(r/v);r%=v})}
 if(sec.k==='ruler'){A[k+'.0']=String(Math.floor(it.mm/10));A[k+'.1']=String(it.mm%10)}
 if(sec.k==='ck')A[k]=it.a.slice();
 if(sec.k==='vcalc')A[k]=String(it.r);
 if(sec.k==='wp'){A[k+'.e']=it.nums[0]+it.op+it.nums[1];A[k+'.n']=String(it.a);A[k+'.u']=it.u}})}"""
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t&&x.t.startsWith('數學習作版面示範'));S.s=i;S.v='sec';render()})()")
    print(pg.inner_text('#app')[300:700])
    pg.click('[data-a=p_go][data-v=z0]')
    n=pg.evaluate("ppSecs().length");rounds=[]
    for si in range(n):
        r=0
        while True:
            pg.evaluate(FILL,si)
            pg.click('[data-a=p_ck]');r+=1
            if pg.locator('[data-a=p_rg]').count() and '過關了' not in pg.inner_text('#app'):
                pg.click('[data-a=p_rg]');continue
            break
        rounds.append(r)
        pg.click('[data-a=p_next]')
    print('rounds',rounds)
    t=pg.inner_text('#app');print(t[:520]);print('分' in t.replace('分鐘',''))
    pg.screenshot(path='shots/sum.png',full_page=True)
    # wrong-first round
    pg.evaluate("(()=>{S.v='sec';S.pp=null;render()})()");print(pg.inner_text('#app')[250:520])
    pg.click('[data-a=p_go][data-v=z0]');pg.evaluate("S.pp.i=7;render()")
    pg.click('[data-a=p_ck]');t=pg.inner_text('#app');print(t[t.find('關卡'):][:120])
    pg.screenshot(path='shots/gate_wrong.png',full_page=True)
    # 國語 demo has no 分
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t&&x.t.startsWith('綜合練習版面示範'));S.s=i;S.v='sec';S.pp=null;render()})()");t=pg.inner_text('#app');print('國語 分:', [l for l in t.split('\n') if '分' in l and '分鐘' not in l][:3])
    pg.click('[data-a=p_go][data-v=z0]');t=pg.inner_text('#app');print([l for l in t.split('\n') if '分' in l][:3])
    print(errs[-1:])
