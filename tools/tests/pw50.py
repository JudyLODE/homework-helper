from playwright.sync_api import sync_playwright
FILL="""si=>{const sec=ppSecs()[si],A=S.pp.a;sec.items.forEach((it,ii)=>{const k=si+'.'+ii;
 if(sec.k==='blk'){it.d.forEach((x,i)=>A[k+'.'+i]=String(x));A[k+'.4']=String(dnum(it.d))}
 if(sec.k==='seq'){it.blank.forEach((b,j)=>A[k+'.'+j]=String(it.v[b]))}
 if(sec.k==='cmp')A[k]=it.a;
 if(sec.k==='ck'){if(it.cir)A[k]=String(it.a[0]);else A[k]=it.a.slice()}
 if(sec.k==='ord'){const w=it.nums.slice().sort((x,y)=>it.dir==='<'?x-y:y-x);w.forEach((x,j)=>A[k+'.'+j]=String(x))}
 if(sec.k==='draw'){let r=it.have!==undefined?it.price-it.have:it.price;if(it.have!==undefined)A[k+'.n']=String(r);DEN.forEach((v,i)=>{A[k+'.q'+i]=Math.floor(r/v);r%=v})}
 if(sec.k==='circ'){const p=circP(it.d);let rem=it.target;const sel=[];let idx=0;it.d.forEach((n,i)=>{let q=Math.min(n,Math.floor(rem/DEN[i]));rem-=q*DEN[i];for(let t=0;t<n;t++){if(t<q)sel.push(idx);idx++}});A[k]=sel}
 if(sec.k==='lkm'){it.a.forEach((v,i)=>A[k+'.'+i]=v)}
 if(sec.k==='mx'){const tk=mxTok(it);let b=-1;it.a.forEach((x,j)=>{let v=x.split('|')[0];if(it.uq.some(g=>g.includes(j))){const g=it.uq.find(g=>g.includes(j));const alts=x.split('|');v=alts[g.indexOf(j)%alts.length]}A[k+'.b'+j]=v});it.c.forEach((x,j)=>A[k+'.c'+j]=String(x));(it.pvn||[]).forEach((n,j)=>String(n).split('').forEach((ch,q)=>A[k+'.p'+j+'_'+q]=ch));if(it.dp!==undefined){let r=it.dp;DEN.forEach((v,i)=>{A[k+'.q'+i]=Math.floor(r/v);r%=v})}}
})}"""
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("(()=>{const i=SEC.findIndex(x=>x.t==='10000 以內的數');S.s=i;S.v='sec';render()})()")
    print(pg.inner_text('#app')[:300])
    print('modes',pg.evaluate("SEC[S.s].m"))
    tot=pg.evaluate("SEC[S.s].pp.z.map(z=>z.secs.reduce((a,x)=>a+ppMax(x),0))")
    print('totals',tot)
    for rep in range(12):
     for zi in range(5):
        pg.evaluate("(zi)=>{ppStart('z'+zi)}",zi)
        n=pg.evaluate("ppSecs().length")
        tot=pg.evaluate("ppSecs().reduce((a,x)=>a+ppMax(x),0)")
        if tot!=100:print('TOTAL',zi,tot)
        for si in range(n):
            pg.evaluate(FILL,si)
            pg.evaluate("()=>{S.pp.ck[S.pp.ver+S.pp.i]=1;render()}")
            sc=pg.evaluate("((si)=>{const sec=ppSecs()[si];return ppSecScore(sec,si)})",si)
            if sc['got']!=sc['max']:
                print('NOT FULL',zi,si,sc,pg.evaluate("JSON.stringify(ppSecs()[%d].items.map(i=>({s:i.s,a:i.a,c:i.c,pvn:i.pvn,o:i.o})))"%si)[:600])
            pg.evaluate("()=>{S.pp.i++}")
    print('errs',[e for e in errs if 'compressed' not in e])
