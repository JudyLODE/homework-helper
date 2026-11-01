from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    print(pg.evaluate("(()=>{const s=SEC.find(x=>x.t&&x.t.startsWith('綜合練習版面示範'));return s?[SEC.indexOf(s),s.pp.o.length,s.pp.z.map(z=>[z.t,z.secs.length,z.secs.map(x=>x.k+':'+x.items.length+':'+ppMax(x)).join(' '),z.secs.reduce((a,x)=>a+ppMax(x),0)])]:null})()"))
    print(errs)
