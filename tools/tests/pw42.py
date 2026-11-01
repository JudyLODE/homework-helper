from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    print(pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t&&x.t.startsWith('數學習作版面示範'));S.s=i;S.v='sec';render();const z=SEC[i].pp.z[0];return [i,z.secs.length,z.secs.map(s=>s.k+':'+s.items.length+':'+ppMax(s)).join(' '),z.secs.reduce((a,s)=>a+ppMax(s),0)]})()"))
    pg.screenshot(path='shots/m_lesson.png',full_page=True)
    pg.click('[data-a=p_go][data-v=z0]')
    # fill all correct per section by computing from data
    res=pg.evaluate("""()=>{
      const secs=ppSecs();const A=S.pp.a;
      secs.forEach((sec,si)=>sec.items.forEach((it,ii)=>{const k=si+'.'+ii;
        if(sec.k==='blk'){it.d.forEach((x,i)=>A[k+'.'+i]=String(x));A[k+'.4']=String(dnum(it.d))}
        if(sec.k==='pv'){[...String(it.n)].forEach((c,i)=>A[k+'.'+i]=c)}
        if(sec.k==='seq'){it.blank.forEach((b,j)=>A[k+'.'+j]=String(it.v[b]))}
        if(sec.k==='cmp')A[k]=it.a;
        if(sec.k==='draw'){let r=it.price;DEN.forEach((v,i)=>{A[k+'.q'+i]=Math.floor(r/v);r%=v})}
        if(sec.k==='ruler'){A[k+'.0']=String(Math.floor(it.mm/10));A[k+'.1']=String(it.mm%10)}
        if(sec.k==='ck')A[k]=it.a.slice();
        if(sec.k==='vcalc')A[k]=String(it.r)
        if(sec.k==='wp'){A[k+'.e']=it.nums[0]+it.op+it.nums[1];A[k+'.n']=String(it.a);A[k+'.u']=it.u}
      }));
      return ppTotal().rows.map(r=>r.got+'/'+r.max).join(' ')+' | '+ppTotal().got+'/'+ppTotal().max}""")
    print(res)
    pg.screenshot(path='shots/m_0.png',full_page=True)
    # walk UI, screenshots each section with answers filled via DOM re-render
    for i in range(9):
        pg.evaluate("i=>{S.pp.i=i;render()}",i)
        pg.click('[data-a=p_ck]')
        pg.screenshot(path=f'shots/m_ck{i}.png',full_page=True)
    # wrong answers case
    pg.evaluate("()=>{S.pp.a={};S.pp.ck={};S.pp.i=7;render()}")
    pg.click('[data-a=p_ck]');pg.screenshot(path='shots/m_wrong7.png',full_page=True)
    pg.evaluate("()=>{S.pp.a={};S.pp.ck={};S.pp.i=8;render()}")
    pg.fill('[data-k="8.0.e"]','785+1260');pg.click('[data-a=p_ck]');pg.screenshot(path='shots/m_wrong8.png',full_page=True)
    # regen
    before=pg.evaluate("JSON.stringify(ppSecs()[7].items.map(x=>[x.a,x.b]))")
    pg.evaluate("()=>{S.pp.a={};S.pp.ck={};S.pp.i=7;render()}")
    pg.click('[data-a=p_rg]');after=pg.evaluate("JSON.stringify(ppSecs()[7].items.map(x=>[x.a,x.b]))");print(before,after)
    print(pg.evaluate("ppSecs()[7].items.map(x=>[x.op,hasCarry(x.op,x.a,x.b)].join()).join(' ')"))
    pg.evaluate("()=>{S.pp.i=8;render()}");pg.click('[data-a=p_rg]');print(pg.evaluate("ppSecs()[8].items.map(x=>x.q).join(' / ')"))
    for i in [0,1,2,3,4,5]:
        pg.evaluate("i=>{S.pp.i=i;render()}",i);pg.click('[data-a=p_rg]')
    print(pg.evaluate("ppSecs().map(s=>s.k+':'+ppMax(s)).join(' ')"))
    print(errs)
