from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.click('[data-a="exam"]');pg.wait_for_timeout(200)
    print(pg.inner_text('#app')[:500])
    # pick all math lessons with templates
    r=pg.evaluate("""()=>{const out=[];for(const sty of ['mid','end']){for(let n=0;n<30;n++){
      const ls=exLessons('math').filter(x=>exHasTpl(x.s)).map(x=>x.i);
      const k=1+Math.floor(Math.random()*ls.length);const sel=shuf2(ls).slice(0,k);
      const secs=exMath(sel,sty);const sp=secs.reduce((a,s)=>a+s.sp,0);const mx=secs.reduce((a,s)=>a+ppMax(s),0);
      out.push([sty,k,secs.length,sp,Math.round(mx*1000)/1000,secs.reduce((a,s)=>a+exUnits(s),0)])}}return out}""")
    bad=[x for x in r if x[3]!=100 or abs(x[4]-100)>1e-6 or x[2]<1]
    print('runs',len(r),'bad',bad[:5]);print(r[:6])
    errs and print(errs)
    print([e for e in errs if 'compressed' not in e])
