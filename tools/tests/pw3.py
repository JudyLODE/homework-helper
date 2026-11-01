import json,re
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(400)
    r=pg.evaluate("""()=>{
      const out={bad:[],cnt:{},samples:[]};
      const mi=SEC.findIndex(s=>s.t==='第15回 二位數乘以一位數'),m2=SEC.findIndex(s=>s.t==='第16回 三位數乘以一位數');
      for(const i of [mi,m2]) for(const lv of ['','1','2','3']) for(const nq of [5,10,20]){
        for(let rep=0;rep<15;rep++){
          S.s=i;S.nq=nq;S.lv=lv;startPr('calc');
          out.cnt[nq+'/'+lv]=S.qs.length;
          if(S.qs.length!==nq)out.bad.push(['len',i,lv,nq,S.qs.length]);
          let prev=0;
          S.qs.forEach(q=>{
            const m=TCH.parse(q);
            let ok=false;
            if(m)ok=m.a*m.b===+q[1];
            else{const e=String(q[0]).match(/(\\d+)\\s*([＋－÷])\\s*(\\d+)/);if(e){const a=+e[1],b=+e[3];ok=(e[2]==='＋'?a+b:e[2]==='－'?a-b:a/b)===+q[1]}}
            if(!ok)out.bad.push(['ans',q[0],q[1]]);
            const L=TG(q[4]).l;if(L<prev)out.bad.push(['order',q[0]]);prev=L;
            if(lv&&q[4]&&TG(q[4]).l!==+lv&&q[4][0]==='v')out.bad.push(['lv',q[4],lv]);
            if(q[4]&&q[4][0]==='v'&&lv&&m&&!lvOK(m.a,m.b,+lv))out.bad.push(['lvOK',q[0],lv]);
          });
        }
      }
      S.s=m2;S.nq=20;S.lv='';startPr('calc');out.samples=S.qs.map(q=>q[4]+' '+q[0]+' = '+q[1]);
      return out}""")
    print('bad',r['bad'][:10],len(r['bad']));print(r['cnt']);print('\n'.join(r['samples'][:20]))
    pg.screenshot(path='shots/calc_new.png')
    # order modes
    for t in ['植物的花、果實、種子','我們的社區']:
        o=pg.evaluate(f"""()=>{{const i=SEC.findIndex(s=>s.t==='{t}');S.s=i;S.nq=10;S.lv='';startPr('order');return S.qs.map(q=>q[0]+'|'+q[2]+'|'+S.tl.length)}}""")
        print(t,o)
        pg.screenshot(path='shots/order_'+t[:2]+'.png')
    # stubbed aiMore
    res=pg.evaluate("""async()=>{
      const mi=SEC.findIndex(s=>s.t==='植物的花、果實、種子');
      const A=norm({sub:'sci',t:'測試自然',w:[['互生','x','🌿']],d:[["題",'','是','因',['否','不']]]});
      const r=ingest([A],'');const idx=r.last;S.s=idx;AI.url='AIzaTEST';
      aiCall=async()=>[{d:[["橘子的種子在哪裡？","","果實裡面","果實包著種子。",["葉子裡","根裡","花裡"],"","v2"],["題",'','是','因',['否','不'],'','v1']],tf:[["番茄是果實。",true,"裡面有種子","","v3"]],so:[["發芽 長葉 開花 結果","過程","v2"]]}];
      S.v='sec';render();document.querySelector('[data-a=more]').click();S.mn=5;S.ml='2';render();
      await aiMore();
      const s=SEC[idx];return {d:s.d.map(x=>x[0]+'/'+x[6]+'/'+x[4].length),tf:s.tf.map(x=>x[4]),so:s.so,m:s.m,msg:document.getElementById('os').textContent}}""")
    print(json.dumps(res,ensure_ascii=False))
    pg.screenshot(path='shots/sec_more.png',full_page=True)
    # quiz tags
    pg.evaluate("S.nq=10;S.lv='';S.s=SEC.findIndex(s=>s.t==='測試自然');startQuiz('talk')");pg.screenshot(path='shots/quiz_tag.png')
    pg.evaluate("S.v='add';render()");pg.screenshot(path='shots/add2.png',full_page=True)
    b.close()
print('ERR',errs)
