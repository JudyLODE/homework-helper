import json
from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(300)
    r=pg.evaluate("""async()=>{
      AI.url='AIzaTEST';
      const i=SEC.findIndex(s=>s.t==='第三課 繞口令村：重點整理');S.s=i;S.v='sec';S.note='';render();
      const orig=SEC[i].d.length;
      aiCall=async()=>[{d:[["「趕＿」，要填哪個字？","","緊","趕緊的緊。",["緊","金","進"].slice(1),"","v3"]],tf:[["新題是非",true,"因","","v3"]],so:[["小明 趕緊 跑向 學校","排成句子","v2"]]}];
      document.querySelector('[data-a=more]').click();
      S.mn=5;S.ml='3';
      await aiMore();
      return {orig:orig,after:SEC[i].d.length,cloneIdx:S.s,cloneTitle:SEC[S.s].t,custom:SEC[S.s].custom,cloneD:SEC[S.s].d.length,note:S.note,v:S.v,home:document.querySelector('.fb.good')&&document.querySelector('.fb.good').textContent}}""")
    print(json.dumps(r,ensure_ascii=False))
    pg.screenshot(path='shots/after_more.png')
    # old sample untouched, clone appears in home list
    print(pg.evaluate("S.v='home';render();document.body.innerText.includes('我的練習')"))
    b.close()
print(errs)
