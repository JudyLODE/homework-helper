import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(300)
    r=pg.evaluate("""()=>{const out={};
     for(const title of ['第三課 繞口令村：重點整理','第三課 綜合練習：字詞與句型','植物的葉、莖、根','植物的花、果實、種子','我們的社區']){
       const i=SEC.findIndex(s=>s.t===title);out[title]={pool:[SEC[i].d.length,SEC[i].tf.length]};
       for(const nq of [5,10,20])for(const lv of ['','1','2','3']){
         S.s=i;S.nq=nq;S.lv=lv;startQuiz('talk');const a=S.qs.map(q=>(q.tag||'-')).join(',');
         startQuiz('tf');const b=S.qs.length;
         out[title][nq+'/'+lv||'x']=S.qs.length+'tf|'+a.split(',').length+'d|'+a.slice(0,40)}
     }
     // verify every d: correct option exists once, ans among options; every tag valid
     const bad=[];SEC0.forEach(s=>{(s.d||[]).forEach(x=>{if(!/^[ov][123]$/.test(x[6]))bad.push(['tag',s.t,x[0]]);if(x[4].includes(x[2]))bad.push(['dup',x[0]]);if(x[5]&&!DIA[x[5]])bad.push(['img',x[5]])});(s.tf||[]).forEach(x=>{if(!/^[ov][123]$/.test(x[4]))bad.push(['tftag',s.t,x[0]]);if(x[3]&&!DIA[x[3]])bad.push(['tfimg',x[3]])})});
     out.bad=bad;return out}""")
    for k,v in r.items():
        print(k, json.dumps(v,ensure_ascii=False) if k!='bad' else v)
    pg.evaluate("S.s=SEC.findIndex(s=>s.t==='第三課 繞口令村：重點整理');S.nq=20;S.lv='';S.v='sec';render()")
    pg.screenshot(path='shots/sec_note.png',full_page=True)
    b.close()
print(errs)
