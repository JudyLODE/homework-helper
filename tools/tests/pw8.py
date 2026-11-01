import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844})
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(300)
    r=pg.evaluate("""()=>{const bad=[];let n=0;
      for(let i=0;i<SEC0.length;i++){const s=SEC[i];
        for(const nq of [5,20])for(const lv of ['','1','3']){S.nq=nq;S.lv=lv;
          try{S.s=i;S.v='sec';render();
            for(const m of s.m.filter(x=>!(x==='paper'&&s.pp&&s.pp.map))){S.s=i;S.mode=m;
              if(m==='cards'){S.v='cards';S.i=0;S.flip=false;render()}
              else if(m==='info'){S.v='info';render()}
              else if(m==='parent'){S.v='parent';render()}
              else if(m==='paper'){S.pp=null;S.v='paper';render();ppStart('o');render();ppStart('h');render()}
              else if(m==='dream'){S.v='dream';S.dj=null;render()}
              else{startQuiz(m);
                 // answer through all questions
                 let g=0;while(!S.done&&g++<60){ if(S.v==='calc'){S.val=String(S.qs[S.i][1]);document.querySelector('[data-a=dchk]').click();document.querySelector('[data-a=dnext]').click()}
                   else if(S.v==='match'){S.done=true}
                   else if(S.v==='order'){S.bt=S.qs[S.i][0].trim().split(/\\s+/).map(w=>S.tl.findIndex((x,k)=>x===w&&!S.bt.includes(k)));
                      /* simple: skip */ S.done=true}
                   else if(S.v==='dict'){S.done=true}
                   else{const q=S.qs[S.i];const k=q.o.findIndex(o=>o.ok);document.querySelector('[data-a=pick][data-k="'+k+'"]').click();document.querySelector('[data-a=nxt]').click()}
                 }
                 render()}
              n++}
          }catch(e){bad.push([s.t,nq,lv,e.message])}
        }}
      return {n,bad:bad.slice(0,8)}}""")
    print(r)
    b.close()
print(errs)
