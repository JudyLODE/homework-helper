import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page()
        await pg.goto('file:///mnt/user-data/outputs/study-helper.html');await pg.wait_for_timeout(1000)
        print(await pg.evaluate("""()=>Object.keys(PPD).map(k=>{const o=normPaper({title:'x',secs:PPD[k].o}),h=normPaper({title:'x',secs:PPD[k].h});
          const diff=[];PPD[k].o.forEach((s,i)=>{const a=o.secs[i],c=h.secs[i];if(!a||a.items.length!==s.items.length)diff.push('o'+i+':'+(a&&a.items.length)+'/'+s.items.length);if(!c||c.items.length!==PPD[k].h[i].items.length)diff.push('h'+i+':'+(c&&c.items.length)+'/'+PPD[k].h[i].items.length)});
          return [k,o.secs.length,h.secs.length,sameShape(o.secs,h.secs),diff]})"""))
        await b.close()
asyncio.run(main())
