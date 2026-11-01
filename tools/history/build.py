import json,re,shutil,sys
F='/mnt/user-data/outputs/study-helper.html'
shutil.copy(F,'/home/claude/study-helper.v58.html') if not __import__('os').path.exists('/home/claude/study-helper.v58.html') else None
s=open('/home/claude/study-helper.v58.html',encoding='utf8').read()   # always rebuild from v58
rd=lambda n:open(n,encoding='utf8').read()
# 1 mx norm svg + render
a="    if(it.tb){const rows=arr(it.tb.rows).map(r=>arr(r).map(one));if(rows.length)o.tb={head:arr(it.tb.head).map(one),rows}}\n"
assert a in s
s=s.replace(a,a+"    {const sv=svgOk(it.svg);if(sv)o.svg=sv}\n",1)
b="${pics}${it.tb?tblHtml"
assert b in s
s=s.replace(b,"${pics}${it.svg||''}${it.tb?tblHtml",1)
# 2 CSS
css=".seg{width:100%;max-width:300px;height:auto;display:block;margin:6px 0}.nlw{display:flex;overflow-x:auto;border-top:3px solid currentColor;padding:6px 0 4px;margin:8px 0}.nlp{flex:0 0 52px;text-align:center;position:relative;padding-top:4px}.nlp i{position:absolute;top:-9px;left:50%;width:2px;height:12px;background:currentColor}.nlp b{display:block;line-height:2.1rem}.nlp .pi{width:2.9rem}\n"
k=s.index('.rl{width:100%;max-width:360px')
j=s.rfind('\n',0,k)+1
s=s[:j]+css+s[j:]
# 3 gens
marker="Object.keys(MATH).forEach(k=>{PT[k]=MATH[k].norm;PTN[k]=MATH[k].name;ppUnits[k]=MATH[k].units});"
assert marker in s
s=s.replace(marker,rd('g1.js')+rd('g2.js')+rd('g3.js')+marker,1)
# 4 lesson literals
def span(txt,title):
    i=txt.index('{"sub":"math","t":"%s"'%title)
    d=0;ins=False;esc=False;j=i
    while True:
        c=txt[j]
        if ins:
            if esc: esc=False
            elif c=='\\': esc=True
            elif c=='"': ins=False
        else:
            if c=='"': ins=True
            elif c=='{': d+=1
            elif c=='}':
                d-=1
                if d==0: return i,j+1
        j+=1
def lesson(t,ic,en,steps):
    o={"sub":"math","t":t,"en":en,"pg":"","ic":ic,"c":"@@C@@","m":["info"],"info":{"h":t+" 解題步驟","r":steps},"w":[],"d":[],"tf":[],"calc":[],"so":[],"mt":[],"parent":[]}
    return json.dumps(o,ensure_ascii=False,separators=(",",":")).replace('"@@C@@"','SUB.math.c')
S2=[["加法直式：相同數位對齊，從個位開始加，滿 10 就進位。","例如 2345＋3126＝5471；個位 5＋6＝11，寫 1 進 1"],
["減法直式：從個位開始減，不夠減就向左邊的位借 1，借來的 1 變成 10。","遇到 0 要連續向左借，例如 6000－2748"],
["先用算式記下來，再用直式算：圈出數字和問題，想一想是「合起來」還是「剩下、比較少」。","「一共」「合起來」「比…多」用加；「還剩」「比…少」「找回」用減"],
["驗算：加法用「和 － 其中一個加數」，看是不是另一個加數；減法用「差 ＋ 減數」，看是不是被減數。","3648＋1952＝5600，驗算 5600－1952＝3648"],
["算算看（　）裡的數：先想清楚（　）是加數、被減數還是減數。","（　）＋1560＝6825 → 6825－1560；7200－（　）＝2020 → 7200－2020"],
["線段圖：整條線代表全部，分成兩段；不知道的那一段用「？」表示。","全部 ＝ 部分 ＋ 部分；部分 ＝ 全部 － 另一部分"],
["看表、看圖解題：先找出題目問的是哪一個數，再從表或圖找出需要的數字。","不夠的錢 ＝ 價錢 － 有的錢；兩條路相差 ＝ 長的 － 短的"]]
S3=[["1 公分 ＝ 10 毫米。尺上每一小格是 1 毫米，每一大格是 1 公分。","3 公分 4 毫米 ＝ 34 毫米；86 毫米 ＝ 8 公分 6 毫米"],
["量長度：物品的左邊對準 0，看右邊對到的刻度，先讀幾公分，再數多幾小格就是幾毫米。","讀到 7，再多 4 小格，就是 7 公分 4 毫米"],
["選單位：很短的用毫米，一般文具、身高用公分，很長的（操場、馬路）用公尺。","鉛筆盒約 20 公分；操場跑道約 200 公尺"],
["長度比大小：先換成同樣的單位（都換成毫米），再比。","10 公分 ＝ 100 毫米，所以 10 公分 ＞ 90 毫米"],
["長度加減：公分和公分、毫米和毫米分開算；毫米滿 10 要換成 1 公分，毫米不夠減要向公分借 1（＝10 毫米）。","5 公分 9 毫米 － 2 公分 8 毫米 ＝ 3 公分 1 毫米"],
["數線：從 0 開始，每一格一樣長，向右越來越大，向左越來越小。","向右走用加，向左走用減；從 4 走到 9，走了 9－4＝5 格"],
["「介於」兩個數之間：比小的大，比大的小。","15 和 18 之間可能是 16 或 17"]]
S4=[["二位數乘以一位數：先算個位，再算十位，滿 10 要記得進位。","例如 23×4＝92；68×6：8×6＝48 寫 8 進 4，6×6＝36 再加 4＝40，答案 408"],
["整十、整百的乘法：先算前面的數字，再補上 0。","60×5＝300；800×7＝5600"],
["三位數乘以一位數：個位、十位、百位依序乘，每一位都要加上進位；中間是 0 也要乘。","806×5：6×5＝30 寫 0 進 3，0×5＝0 加 3＝3，8×5＝40，答案 4030"],
["應用題：看到「每…有…」「一共幾個」，想一想是不是同樣多的東西合起來，用乘法。","一盒 24 個，賣 9 盒 → 24×9＝216"],
["乘法估算：把數字想成接近的整十或整百，再乘，就知道答案大約是多少。","399×7 ≈ 400×7＝2800；51×6 ≈ 50×6＝300"],
["估算夠不夠、會不會比較便宜：先估算，再和錢（或數量）比一比。","395 元的草莓買 6 箱 ≈ 400×6＝2400，比 2000 多，所以 2000 元不夠"],
["比大小：乘數一樣時，比被乘數就好；不一樣就先算出答案再比。","200×5 ＜ 202×5，因為乘數都是 5，202 比 200 大"],
["檢查有沒有算錯：用估算看大小對不對，再檢查進位有沒有加上。","245×7 約是 250×7＝1750，答案不會是 4295"]]
S5=[["這一課是第 1～4 單元的綜合練習：10000 以內的數、加減、長度（毫米）、乘法。","遇到不會的題目，可以回去看前面每一課的「解題步驟」"],
["讀題時先圈出數字和問題，想一想要用加、減還是乘。","「一共」用加、「剩下」「相差」用減、「每…有…，共…」用乘"],
["算完要檢查：先估算看看大小對不對，加減還可以驗算。","3648＋1952＝5600，驗算 5600－1952＝3648"],
["換算單位時先想：1 公分 ＝ 10 毫米。","3 公分 4 毫米 ＝ 34 毫米"],
["比大小、排順序：先看位數，再從最高位比起。","6120 ＞ 6012，因為百位 1 ＞ 0"]]
for t,ic,en,st in [("10000 以內的加減","➕","",S2),("毫米與數線","📏","",S3),("乘法","✖️","含二位數、三位數乘以一位數",S4)]:
    i,j=span(s,t); s=s[:i]+lesson(t,ic,en,st)+s[j:]
i,j=span(s,"乘法")
s=s[:j]+',\n'+lesson("第 1～4 單元綜合評量","🏁","",S5)+s[j:]
# 5 PRIV + installers
M1END="/*PRIV:M1:END*/\n"
assert M1END in s
priv=''.join(rd('priv_m%d.js'%n) for n in (2,3,4,5))
s=s.replace(M1END,M1END+priv,1)
oldinst="(function(){try{const L=SEC.find(s=>s.sub==='math'&&s.t==='10000 以內的數');"
assert oldinst in s
inst="""(function(){try{[['10000 以內的加減','makePrivM2'],['毫米與數線','makePrivM3'],['乘法','makePrivM4'],['第 1～4 單元綜合評量','makePrivM5']].forEach(([t,fn])=>{try{const L=SEC.find(s=>s.sub==='math'&&s.t===t),f=({makePrivM2:typeof makePrivM2==='function'?makePrivM2:0,makePrivM3:typeof makePrivM3==='function'?makePrivM3:0,makePrivM4:typeof makePrivM4==='function'?makePrivM4:0,makePrivM5:typeof makePrivM5==='function'?makePrivM5:0})[fn];if(!L||!f)return;const z=f();if(!z.length)return;L.m=['info','paper'];L.pp={title:'數學習作',o:[],h:[],q:[],z,src:1,vf:1,map:1,zp:1,zl:'習作',rg:1}}catch(e){try{console.warn('priv',t,e)}catch(_){}}})}catch(e){}})();
"""
s=s.replace(oldinst,inst+oldinst,1)
s=s.replace('v58','v59') if False else s
open(F,'w',encoding='utf8').write(s)
print('built',len(s))
