from playwright.sync_api import sync_playwright
JS="""(()=>{
const i=SEC.findIndex(x=>x.t&&x.t.startsWith('綜合練習版面示範'));S.s=i;S.v='sec';render();const out=[];
['z0','z1','z2'].forEach(ver=>{
 ppStart(ver);const secs=ppSecs();
 secs.forEach((sec,si)=>sec.items.forEach((it,ii)=>{const k=si+'.'+ii;
  switch(sec.k){
   case 'write':{const tk=wparse(it.s).filter(x=>x.m);tk.forEach((x,j)=>S.pp.a[k+'.'+j]=it.a[j]);break}
   case 'pick':it.a.forEach((v,j)=>S.pp.a[k+'.'+j]=v);break;
   case 'fill':it.a.forEach((v,j)=>S.pp.a[k+'.'+j]=v);break;
   case 'rad2':S.pp.a[k+'.r']=it.b+'部';it.cs.forEach((c,j)=>{S.pp.a[k+'.w'+j]=c+'子';S.pp.pc[k+'.w'+j]=1});break;
   case 'tfx':S.pp.a[k]=it.a?1:0;break;
   case 'like':{const n=(it.tpl.match(blankRe)||[]).length;for(let j=0;j<n;j++){S.pp.a[k+'.'+j]='X';S.pp.pc[k+'.'+j]=1}break}
   case 'sent':S.pp.a[k]='句子';S.pp.pc[k]=1;break;
   case 'fix':{[...it.a].forEach((ch,j)=>S.pp.a[k+'.t'+j]=ch);S.pp.a[k+'.c']=fixPos(it.s,it.w);break}
   case 'bank':it.a.forEach((v,j)=>S.pp.a[k+'.'+j]=v);break;
   case 'cls':S.pp.a[k]=it.a;break;
   case 'link':S.pp.a[k]=ii;break;
  }}));
 secs.forEach((x,i)=>S.pp.ck[ver+i]=1);
 const T=ppTotal();out.push([ver,T.got,T.max,T.rows.filter(r=>r.got!==r.max).map(r=>r.t+':'+r.got+'/'+r.max)]);
});
return out})()"""
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    print(pg.evaluate(JS));print(errs)
