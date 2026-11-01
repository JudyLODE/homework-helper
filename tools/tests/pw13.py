import asyncio,json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={'width':430,'height':900})
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1200)
        r=await pg.evaluate("""()=>{const out=[];SEC.filter(s=>sk(s)==='cn').forEach(s=>{(s.w||[]).forEach(x=>{
          const zh=x[1].split('｜')[0].trim().split(/\\s+/);const cs=[...x[0]].filter(c=>/[\\u4e00-\\u9fff]/.test(c));
          if(zh.length!==cs.length){out.push([s.t,x[0],x[1],'長度不同']);return}
          cs.forEach((c,i)=>{const z=zyAll(c);if(!z)out.push([s.t,x[0],c,'辭典無此字']);else if(!z.includes(zh[i])&&!z.includes('˙'+zh[i]))out.push([s.t,x[0],c,zh[i],z.join('/')])})})});return out}""")
        for x in r:print(x)
        print('cn word check done',len(r))
        # mt radicals/parts and words in mt
        m=await pg.evaluate("SEC.filter(s=>sk(s)==='cn').map(s=>[s.t,(s.mt||[]).map(x=>x.join('=>'))])");print(m)
        print(errs)
        await b.close()
asyncio.run(main())
