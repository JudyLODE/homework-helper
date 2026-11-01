import asyncio,json,base64
from playwright.async_api import async_playwright
PDF='/mnt/user-data/attachments/d7dced68-e677-552b-8070-720d7f141e4d/7e4701b1-___________________.pdf'
IM1='/mnt/user-data/attachments/d7dced68-e677-552b-8070-720d7f141e4d/59076b4e-image.png'
IM2='/mnt/user-data/attachments/d7dced68-e677-552b-8070-720d7f141e4d/882c2159-image.png'
LIB='/opt/npm-tools/node_modules/pdfjs-dist/legacy/build/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={'width':430,'height':900})
        pg=await ctx.new_page()
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        async def serve(route):
            u=route.request.url;f=LIB+u.split('/')[-1]
            await route.fulfill(path=f,content_type='text/javascript',headers={'access-control-allow-origin':'*'})
        await pg.route('https://pdfjs.test/*',serve)
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1200)
        await pg.evaluate("""async()=>{const m=await import('https://pdfjs.test/pdf.min.mjs');m.GlobalWorkerOptions.workerSrc='https://pdfjs.test/pdf.worker.min.mjs';window.pdfjsLib=m;}""")
        await pg.evaluate("""()=>{
          window.__calls=[];
          const base=PPD.c5;
          const bad=JSON.parse(JSON.stringify(base.o));
          bad.forEach(sec=>{ if(sec.k==='rad')sec.items[0].r='木'; if(sec.k==='zy')sec.items[2].a=0; });
          const hard=JSON.parse(JSON.stringify(base.h));
          window.__mode='ok';
          SMP={limits:async()=>({images:{maxCount:8}}),json:async(prompt,opts)=>{
            __calls.push({hard:prompt.includes('原卷：'),imgs:opts&&opts.images?opts.images.length:0,types:opts&&opts.images?opts.images.map(x=>x.type+':'+x.size):[]});
            if(prompt.includes('原卷：')){ if(__mode==='short'){const h=JSON.parse(JSON.stringify(hard));h.pop();return {lessons:[{title:'x',secs:h}]}} return {lessons:[{title:base.title,secs:hard}]}}
            return {lessons:[{sub:'cn',title:'國小國語三上單課卷：第五課 飛舞的絲帶',secs:bad}]}}};
          S.v='add';S.asub='cn';S.amat='paper';render();}""")
        await pg.set_input_files('#ph',[IM1,IM2,PDF])
        await pg.wait_for_timeout(500)
        print('preview html has pdf:',await pg.evaluate("document.getElementById('pv').innerText.slice(0,80)"))
        await pg.screenshot(path='/home/claude/shots/pp_add.png',full_page=True)
        await pg.click('[data-a="ai"]')
        await pg.wait_for_timeout(15000)
        print('status:',await pg.evaluate("[S.v,(document.getElementById('os')||{}).textContent,JSON.stringify(window.__calls||[]).slice(0,300)]"))
        await pg.screenshot(path='/home/claude/shots/pp_dbg.png',full_page=True)
        await pg.wait_for_function("S.v==='sec'",timeout=60000)
        calls=await pg.evaluate('__calls');print(json.dumps(calls,ensure_ascii=False))
        r=await pg.evaluate("""()=>{const s=SEC[S.s];return {t:s.t,m:s.m,o:s.pp.o.length,h:s.pp.h.length,fx:s.pp.fx,src:s.pp.src,rad:s.pp.o.find(x=>x.k==='rad').items[0].r,zy:(()=>{const it=s.pp.o.find(x=>x.k==='zy').items[2];return it.o[it.a]})(),note:S.note,ls:LS.length}}""")
        print(r)
        await pg.screenshot(path='/home/claude/shots/pp_sec_new.png',full_page=True)
        # hard failing shape
        await pg.evaluate("__mode='short'")
        await pg.evaluate("()=>{PF=[];S.v='add';S.asub='cn';S.amat='paper';render()}")
        await pg.set_input_files('#ph',[IM1])
        await pg.click('[data-a="ai"]')
        await pg.wait_for_function("S.v==='sec'",timeout=60000)
        print('short-hard:',await pg.evaluate("[SEC[S.s].pp.h.length,S.note]"))
        # PDF-only with no SMP images fail
        print('errs',errs)
        await b.close()
asyncio.run(main())
