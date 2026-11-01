import sys,json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(500)
    print(pg.evaluate("SEC.map((s,i)=>i+':'+s.t).join(' | ')"))
    idx=lambda t:pg.evaluate("t=>SEC.findIndex(s=>s.t===t)",t)
    # --- science
    si=idx('植物的葉、莖、根');pj=idx('植物的花、果實、種子')
    for name,i in [('sci1',si),('sci2',pj)]:
        pg.evaluate(f"S.s={i};S.v='sec';render()")
        pg.evaluate("S.v='info';render()");pg.screenshot(path=f'shots/{name}_info.png',full_page=True)
        n=pg.evaluate(f"SEC[{i}].w.length")
        for k in range(n):
            pg.evaluate(f"S.v='cards';S.i={k};S.flip=false;render()")
            pg.screenshot(path=f'shots/{name}_card{k}.png')
    # quiz feedback with image
    pg.evaluate(f"S.s={si};startQuiz('talk')")
    pg.evaluate("S.qs=S.qs.filter(q=>q.img);S.i=0;S.pick=0;render()");pg.screenshot(path='shots/sci_quiz_img.png',full_page=True)
    # --- math
    mi=idx('第15回 二位數乘以一位數');m2=idx('第16回 三位數乘以一位數')
    cnt=0
    for i in (mi,m2):
        pg.evaluate(f"S.s={i};startPr('calc')")
        n=pg.evaluate("S.qs.length")
        for q in range(n):
            pg.evaluate(f"S.i={q};S.pick=null;S.teach=0;S.hint=false;S.val='';render()")
            if q==0 and i==mi:pg.screenshot(path='shots/calc_q0.png')
            pg.click('[data-a=teach]')
            m=pg.evaluate("S.ts.length")
            for st in range(m):
                if i==m2 and q==5 or (i==mi and q in(0,3)):pg.screenshot(path=f'shots/t_{i}_{q}_{st}.png',full_page=True)
                cnt+=1
                if st<m-1:pg.click('[data-a=tnext]')
            ans=pg.evaluate("S.ts[S.ts.length-1].st.res.slice().reverse().join('')")
            exp=pg.evaluate("String(S.qs[S.i][1])")
            print(i,q,m,ans,exp,'OK' if ans==exp else 'BAD')
            pg.click('[data-a=tnext]')
            assert pg.evaluate("S.teach")==0
    print('steps viewed',cnt)
    b.close()
print('ERRORS',errs)
