import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(400)
    # simulate AI output (no diagram keys, duplicates, 2 lessons same subject) as any AI would return
    r=pg.evaluate("""()=>{
      const A={sub:'sci',t:'植物 A',w:[['互生','1節1片','🌿'],['節','葉子位置','📍'],['互生','重複','🌿'],['輪生','3片以上','🎡']],d:[["題1","","是","因",["否","不"]],["題1","","是","因",["否","不"]]],tf:[["敘述1",true,"因"]],mt:[["a","b"],["a","b"],["c","d"],["e","f"]],parent:["做這個"]};
      const B={sub:'sci',t:'植物 B',w:[['鬚根','很多細根','🌾'],['互生','又一次','🌿'],['蚯蚓','不在圖庫','🪱']],d:[["題2","","是","因",["否","不"]]],parent:["做這個"]};
      const C={sub:'math',t:'數學',calc:[["36 × 2 ＝ ？",72,"",["36 × 2"]],["36 × 2 ＝ ？",72,"",["36 × 2"]]],w:[]};
      const n0=SEC.length;
      const list=[A,B,C].map(norm);
      const r1=ingest(list,'');
      const sci=SEC.find(s=>s.custom&&s.sub==='sci');
      const out={added:SEC.length-n0,count:r1.count,w:sci.w.map(x=>x[0]+':'+(x[3]||'-')),d:sci.d.length,mt:sci.mt.length,parent:sci.parent.length,m:sci.m,
        math_calc:SEC.find(s=>s.custom&&s.sub==='math').calc.length};
      // second upload same day same subject -> merged into existing
      const D={sub:'sci',t:'植物 C',w:[['雌蕊','x','🌷'],['互生','再重複','🌿']]};
      const r2=ingest([norm(D)],'');
      out.after2=SEC.length-n0;out.w2=sci.w.map(x=>x[0]).join(',');
      // forced subject: AI mislabeled as en
      const E={sub:'en',t:'國語',w:[['詞語','注音｜意思','📖']]};
      const r3=ingest([norm(E)],'cn');out.forced=SEC[r3.last].sub+'/'+SEC[r3.last].lang;
      return out}""")
    print(json.dumps(r,ensure_ascii=False))
    # UI: add page chips + parent guide
    pg.evaluate("S.v='add';render()")
    pg.click('#sc [data-f=math]');print('asub',pg.evaluate("S.asub"),pg.evaluate("document.querySelector('#sc .chip.on').textContent"))
    pg.screenshot(path='shots/add.png',full_page=True)
    pg.evaluate("S.v='home';render()")
    pg.evaluate("document.querySelectorAll('details.how').forEach(d=>d.open=true)")
    pg.screenshot(path='shots/parent.png',full_page=True)
    b.close()
print('ERR',errs)
