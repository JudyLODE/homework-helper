from playwright.sync_api import sync_playwright
import json
W=lambda s,k,items:{'k':k,'t':s,'d':'（每格2分，共8分）','pt':2,'items':items}
base=[W('一、寫國字或注音','write',[{'s':'他很【ㄏㄨㄛˇ】動。','a':['活']}]*4)]
def pj(unit,kind,secs): return {'unit':unit,'kind':kind,'secs':secs}
resp=[
 pj('第一課','基礎篇',[W('一、寫國字或注音','write',[{'s':'今天是【ㄒㄧㄥ】期天。','a':['星']},{'s':'我們去〖湖〗邊。','a':['ㄏㄨˊ']},{'s':'小明很【ㄍㄠ】興。','a':['高']},{'s':'他在〖唱〗歌。','a':['ㄔㄤˋ']}]),
   W('二、連一連','link',[{'l':'日加月','r':'明'},{'l':'木加木','r':'林'}]),
   {'k':'fill','t':'三、看圖填空','d':'（每格3分，共6分）','pt':3,'items':[{'s':'圖裡有一隻（ ），牠在（ ）。','a':['貓','睡覺'],'svg':'<svg viewBox="0 0 240 150"><rect width="240" height="150" fill="#eef"/><script>alert(1)</script></svg>'}]}]),
 pj('第一課','進階篇',[W('一、改錯別字','fix',[{'s':'我們立用時間。','w':'立','a':'利'}])]),
 pj('第一課','重點整理',[]),
 pj('第二課','基礎篇',[W('一、選擇','mc',[{'q':'哪個是動物？','o':['桌','貓','筆','書'],'a':1,'why':'貓是動物'}])]),
 pj('閱讀階梯一','綜合練習',[{'k':'txt','t':'短文','pt':1,'items':[{'p':'小明去公園。'}]},W('一、回答','mc',[{'q':'誰去公園？','o':['小明','小華'],'a':0,'why':'短文'}])]),
 pj('閱讀階梯一','綜合練習',[W('二、是非','tfx',[{'s':'小明去學校。','a':False,'why':'去公園'}])]),
 'BAD',
]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':430,'height':900})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/study-helper.html');pg.wait_for_timeout(900)
    pg.evaluate("""r=>{window.__q=r.slice();AI.url='x';shrink=async()=>'data:image/jpeg;base64,AA==';aiCall=async()=>{const x=window.__q.shift();if(x==='BAD')throw 'boom';return x};
      S.v='add';S.asub='cn';S.amat='work';render();PF=r.map((_,i)=>({name:i+'.png',type:'image/png'}))}""",resp)
    pg.evaluate("aiZP()");pg.wait_for_function("S.note||document.getElementById('os')&&/oops/.test(document.getElementById('os').className)",timeout=30000)
    print(pg.evaluate("S.note"));print(pg.evaluate("document.getElementById('os')&&document.getElementById('os').textContent"))
    print(pg.evaluate("SEC.filter(s=>s.pp&&s.pp.zp).map(s=>[s.t,s.pp.z.map(z=>z.t+':'+z.secs.length+':'+z.secs.map(x=>x.k+x.items.length).join(',')),JSON.stringify(s.pp.z[0].secs.find(x=>x.k==='fill')&&s.pp.z[0].secs.find(x=>x.k==='fill').items[0].svg)])"))
    pg.evaluate("S.s=SEC.findIndex(s=>s.t==='第一課 學習評量');S.v='sec';render()");print(pg.inner_text('#app')[:400])
    pg.evaluate("S.v='home';S.f='cn';render()");t=pg.inner_text('#app');i=t.find('第一課');print(t[i-50:i+900])
    pg.screenshot(path='shots/zp_home.png',full_page=True)
    print(errs)
