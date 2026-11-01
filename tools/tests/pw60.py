from playwright.sync_api import sync_playwright
import json,sys
TT=['10000 以內的加減','毫米與數線','乘法','第 1～4 單元綜合評量']
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:errs.append('C:'+m.text) if m.type in('warning','error') else None)
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    r=pg.evaluate("""(TT)=>{const out=[],tot=[];
     TT.forEach(T=>{const L=SEC.find(x=>x.t===T);if(!L||!L.pp){out.push(['NOLESSON',T]);return}
     L.pp.z.forEach((z,zi)=>{let sum=0;z.secs.forEach((sec,si)=>{const M0=MATH[sec.k];
       sec.items.forEach((it,ii)=>{sum+=sec.pt*ppUnits[sec.k](sec,it);
        const u0=ppUnits[sec.k](sec,it);let bad=0,nul=0,same=0,uh=0;
        for(let t=0;t<200;t++){let g;try{g=M0.gen?M0.gen(it):it}catch(e){bad++;continue}
          if(!M0.gen){nul=-1;break}
          let n=null;try{n=M0.norm(g)}catch(e){}
          if(!n){nul++;continue}
          if(ppUnits[sec.k](sec,n)!==u0)uh++;
          if(JSON.stringify(n)===JSON.stringify(it))same++}
        if(bad||nul||uh)out.push([T,z.t,si+1,sec.k,ii+1,'err',bad,'null',nul,'unitsDiff',uh,'same',same])}) });tot.push([z.t,Math.round(sum*100)/100])}) });return {out,tot}}""",TT)
    for x in r['out']:print('PROBLEM',x)
    for x in r['tot']:print(x)
    print([e for e in errs if 'compressed' not in e][:10])
