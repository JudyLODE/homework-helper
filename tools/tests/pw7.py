import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844})
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(300)
    r=pg.evaluate("""async()=>{const out=[];AI.url='AIzaTEST';
      aiCall=async()=>[{d:[["新題X","","是","因",["否","不","無"],"","v2"]],tf:[["新是非X",true,"因","","v1"]]}];
      const n=SEC0.length;
      for(let i=0;i<n;i++){
        S.s=i;S.v='sec';S.note='';S.mn=5;S.ml='';render();
        try{await aiMore();out.push([SEC0[i].t,S.note.slice(0,14),SEC[S.s].custom,SEC[S.s].d.length])}catch(e){out.push([SEC0[i].t,'ERR '+e.message])}
      }
      return out}""")
    for x in r:print(x)
    b.close()
print(errs)
