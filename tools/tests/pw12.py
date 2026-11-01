import asyncio
from playwright.async_api import async_playwright
PDF='/mnt/user-data/attachments/d7dced68-e677-552b-8070-720d7f141e4d/7e4701b1-___________________.pdf'
LIB='/opt/npm-tools/node_modules/pdfjs-dist/legacy/build/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page()
        pg.on('console',lambda m:print('C',m.type,m.text[:200]))
        async def serve(route):
            await route.fulfill(path=LIB+route.request.url.split('/')[-1],content_type='text/javascript',headers={'access-control-allow-origin':'*'})
        await pg.route('https://pdfjs.test/*',serve)
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(800)
        await pg.evaluate("""async()=>{const m=await import('https://pdfjs.test/pdf.min.mjs');m.GlobalWorkerOptions.workerSrc='https://pdfjs.test/pdf.worker.min.mjs';window.pdfjsLib=m;}""")
        pg2=pg
        await pg.set_content('<input id=f type=file>') if False else None
        r=await pg.evaluate("""async(b64)=>{const bin=Uint8Array.from(atob(b64),c=>c.charCodeAt(0));const f=new File([bin],'a.pdf',{type:'application/pdf'});try{const o=await pdfImgs(f);return {n:o.length,len:o.map(x=>x.length)}}catch(e){return 'ERR '+(e&&e.message||e)}}""",__import__('base64').b64encode(open(PDF,'rb').read()).decode())
        print(r)
        await b.close()
asyncio.run(main())
