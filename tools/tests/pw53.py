from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    r=pg.evaluate("""()=>{const L=SEC.find(x=>x.t==='10000 以內的數');const out=[];
     L.pp.z.forEach((z,zi)=>z.secs.forEach((sec,si)=>{const M0=MATH[sec.k];
       sec.items.forEach((it,ii)=>{
        const u0=ppUnits[sec.k](sec,it);let bad=0,nul=0,same=0,uh=0;
        for(let t=0;t<300;t++){let g;try{g=M0.gen?M0.gen(it):it}catch(e){bad++;continue}
          if(!M0.gen){nul=-1;break}
          let n=null;try{n=M0.norm(g)}catch(e){}
          if(!n){nul++;continue}
          if(ppUnits[sec.k](sec,n)!==u0)uh++;
          if(JSON.stringify(n)===JSON.stringify(it))same++}
        out.push([zi+1,si+1,sec.k,ii+1,u0,'err',bad,'null',nul,'unitsDiff',uh,'same',same])}) }));return out}""")
    for x in r:
        if x[6] or x[8] or x[10]:print('PROBLEM',x)
    print(len(r),'items checked')
    print([e for e in errs if 'compressed' not in e])
