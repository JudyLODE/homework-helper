/* ===== 第二批換題：應用題情境庫、數線、算式、線段圖（加減／長度／乘法單元共用） ===== */
const NM1=()=>pick1(NAMES);
const WPT={
 add:[
  {q:'{N}騎單車遊舊草嶺隧道，已經騎了 {A} 公尺，再騎 {B} 公尺就出隧道口，這座隧道全長幾公尺？',u:'公尺',op:'+',r:[[400,3200],[400,3200]]},
  {q:'農場昨天採收了 {A} 顆高麗菜，今天又採收了 {B} 顆，兩天一共採收了幾顆高麗菜？',u:'顆',op:'+',r:[[900,5200],[900,4800]]},
  {q:'遊樂場上午賣出 {A} 張門票，下午賣出 {B} 張，上午和下午共賣出多少張門票？',u:'張',op:'+',r:[[1500,5600],[1500,4000]]},
  {q:'一雙直排輪鞋 {A} 元，一套護具 {B} 元。{N}買一雙直排輪鞋和一套護具，要付幾元？',u:'元',op:'+',r:[[1800,4800],[700,2400]]},
  {q:'郵差上星期運送了 {A} 個包裹，這星期運送的數量比上星期多 {B} 個，這星期郵差運送了幾個包裹？',u:'個',op:'+',r:[[2800,6800],[500,2400]]},
  {q:'一臺微波爐 {A} 元，一個電鍋比一臺微波爐貴 {B} 元，一個電鍋要幾元？',u:'元',op:'+',r:[[900,4200],[300,1800]]},
  {q:'果園今年收成了 {A} 顆水梨，比去年多 {B} 顆，去年收成了多少顆水梨？',u:'顆',op:'+',sub:1,r:[[2000,4800],[300,1800]]},
  {q:'{N}家的書店有 {A} 本故事書和 {B} 本漫畫，書店裡共有幾本書？',u:'本',op:'+',r:[[900,5200],[900,4200]]}],
 sub:[
  {q:'{N}有 {A} 元，買了一枝 {B} 元的羽毛球拍，還剩下多少元？',u:'元',op:'-',r:[[2000,6000],[600,1900]]},
  {q:'球池裡有 {A} 顆紅球，綠球比紅球少 {B} 顆，球池裡有幾顆綠球？',u:'顆',op:'-',r:[[3000,7200],[600,2400]]},
  {q:'寶瓶星號郵輪一次可載客 {A} 人，這次行程還有 {B} 人的空位，這次行程有多少人參加？',u:'人',op:'-',r:[[1000,2400],[80,600]]},
  {q:'甜點工廠生產了 {A} 盒布丁，賣出 {B} 盒，還剩下幾盒？',u:'盒',op:'-',r:[[4000,8800],[1200,3800]]},
  {q:'媽媽買了一支吹風機，付了 {A} 元，找回 {B} 元，一支吹風機是多少元？',u:'元',op:'-',r:[[2000,5000],[200,900]]},
  {q:'演唱會門票限量 {A} 張，已賣出 {B} 張，還剩下幾張未賣出？',u:'張',op:'-',r:[[3000,6000],[1200,3800]]},
  {q:'爺爺上星期採收了 {A} 個橘子，這星期採收的數量比上星期少 {B} 個，這星期採收了多少個橘子？',u:'個',op:'-',r:[[3000,6000],[500,1500]]},
  {q:'一輛腳踏車 {A} 元，促銷期間便宜 {B} 元，買一輛腳踏車要付多少元？',u:'元',op:'-',r:[[3000,6000],[600,1900]]},
  {q:'爸爸買了一張高鐵票花了 {B} 元，爸爸付了 {A} 元，可以找回幾元？',u:'元',op:'-',r:[[3000,5000],[1600,2900]]},
  {q:'動物園上午入園 {A} 人，下午比上午少 {B} 人，下午入園人數是幾人？',u:'人',op:'-',r:[[3000,6000],[700,2400]]},
  {q:'爸爸參加 {A} 公尺跑步比賽，剩 {B} 公尺就抵達終點，爸爸已經跑了多少公尺？',u:'公尺',op:'-',r:[[2000,5000],[600,1500]]},
  {q:'球場有 {A} 個座位，球賽開始，一人坐一個座位，座位全部坐滿後，還有 {B} 人站著，有多少人觀看球賽？',u:'人',op:'+',r:[[3000,8000],[300,900]]}],
 orig:[
  {q:'{N}有一些錢，買菜花了 {A} 元後，還剩下 {B} 元，{N}原來有多少元？',u:'元',op:'+',sg:1,r:[[300,1600],[300,1600]]},
  {q:'爸爸買了一些燈泡，用了 {A} 個布置聖誕樹，剩下 {B} 個，爸爸原來買了幾個燈泡？',u:'個',op:'+',sg:1,r:[[2000,5200],[2000,4800]]},
  {q:'{N}有一些點數，兌換一個籃球後，還剩下 {B} 點，籃球要 {A} 點，{N}原來有幾點？',u:'點',op:'+',sg:1,r:[[900,1600],[90,600]]},
  {q:'農場原來有一些樹，今年又種了 {A} 棵後，現在共有 {B} 棵，農場裡原來有幾棵樹？',u:'棵',op:'-',sw:1,sg:1,r:[[1800,3600],[4200,8400]]}],
 unk:[
  {q:'工廠早上生產了 {A} 輛車，下午又生產了一些，共生產了 {B} 輛車，下午生產了幾輛車？',u:'輛',op:'-',sw:1,sg:1,r:[[1800,3200],[3600,6400]]},
  {q:'摸彩箱裡有 {A} 張摸彩券，抽出一些後，箱子裡還有 {B} 張，是抽出了幾張摸彩券？',u:'張',op:'-',sg:1,r:[[2000,5000],[600,1800]]},
  {q:'{N}預計走 {A} 步，上午走了一些，還有 {B} 步沒走，他上午走了幾步？',u:'步',op:'-',sg:1,r:[[4000,8000],[1500,3800]]},
  {q:'動物園買了 {A} 籃水果，動物吃掉一些後，還剩下 {B} 籃，動物吃掉了多少籃水果？',u:'籃',op:'-',sg:1,r:[[1000,2400],[300,900]]},
  {q:'{N}有一些點數，還需要 {B} 點才能兌換一個 {A} 點的手環，{N}現在有幾點？',u:'點',op:'-',sg:1,r:[[3000,5000],[300,900]]}],
 mul2:[
  {q:'一張捷運車票 {A} 元，買 {B} 張共要付多少元？',u:'元',op:'×',r:[[11,99],[2,9]]},
  {q:'一杯珍珠奶茶 {A} 元，阿姨買了 {B} 杯，要付幾元？',u:'元',op:'×',r:[[30,99],[2,9]]},
  {q:'一盒水餃有 {A} 個，老闆今天賣出 {B} 盒，共賣出幾個水餃？',u:'個',op:'×',r:[[12,48],[2,9]]},
  {q:'一列火車有 {B} 個車廂，每個車廂有 {A} 個座位，一列火車有幾個座位？',u:'個',op:'×',r:[[30,99],[3,9]]},
  {q:'一包紙平分給 {B} 個小朋友，每個小朋友分到 {A} 張，這包紙共有幾張？',u:'張',op:'×',r:[[30,99],[3,9]]},
  {q:'一盒巧克力賣 {A} 元，老師買了 {B} 盒，要付幾元？',u:'元',op:'×',r:[[30,99],[2,9]]},
  {q:'一包氣球 {A} 元，{N}買了 {B} 包氣球，要付幾元？',u:'元',op:'×',r:[[25,99],[2,9]]},
  {q:'{N}每天練習跳繩 {A} 下，連續跳了 {B} 天，共跳繩了幾下？',u:'下',op:'×',r:[[20,99],[3,9]]},
  {q:'一箱洋芋片有 {A} 包，商店進貨 {B} 箱洋芋片，共有幾包？',u:'包',op:'×',r:[[12,48],[3,9]]},
  {q:'一本書有 {A} 頁，{N}每天看同樣多的頁數，看了 {B} 天剛好看完，這本書共有幾頁？',u:'頁',op:'×',r:[[24,48],[3,9]]}],
 mul3:[
  {q:'一包影印紙 {A} 張，學校上個月用了 {B} 包，是用了幾張影印紙？',u:'張',op:'×',r:[[200,990],[2,9]]},
  {q:'一桶瓦斯 {A} 元，小吃店老闆上個月買了 {B} 桶，共花費多少元？',u:'元',op:'×',r:[[200,990],[2,9]]},
  {q:'一張電影票 {A} 元，爸爸買了 {B} 張，要付幾元？',u:'元',op:'×',r:[[120,480],[3,9]]},
  {q:'一份炸雞套餐 {A} 元，慶生會老師買了 {B} 份，要付幾元？',u:'元',op:'×',r:[[210,480],[3,9]]},
  {q:'一捲衛生紙有 {A} 張，一袋有 {B} 捲，一袋衛生紙共有幾張？',u:'張',op:'×',r:[[210,480],[3,9]]},
  {q:'一桶軟糖 {A} 元，校長買了 {B} 桶，共要付幾元？',u:'元',op:'×',r:[[210,480],[3,9]]},
  {q:'一捲緞帶長 {A} 公分，老師買了 {B} 捲，這些緞帶共長幾公分？',u:'公分',op:'×',r:[[120,480],[3,9]]},
  {q:'一瓶優酪乳 {A} 元，爺爺拿了 {B} 瓶，要付幾元？',u:'元',op:'×',r:[[110,480],[3,9]]}]
};
function wpGen(kind,pa){pa=pa||{};const L=WPT[kind];if(!L)return null;const T=pick1(L);
  for(let t=0;t<400;t++){let x=rnd(T.r[0][0],T.r[0][1]),y=rnd(T.r[1][0],T.r[1][1]),nums;
    if(kind==='mul2'&&Math.random()<.25)x=Math.floor(x/10)*10||10;if(kind==='mul3'&&Math.random()<.2)x=Math.floor(x/100)*100;
    if(T.op==='-'){const big=Math.max(x,y),sm=Math.min(x,y);if(big-sm<50)continue;if(T.sw){x=sm;y=big}else{x=big;y=sm}nums=[big,sm]}
    else if(T.op==='+'){if(x+y>9999)continue;nums=[x,y]}
    else{if(x*y>9999)continue;nums=[x,y]}
    const n1=NM1();const q=T.q.replace(/\{N\}/g,n1).replace('{A}',x).replace('{B}',y);
    return {q,nums,op:T.op,u:T.u,wk:kind,sg:pa.sg?1:0}}
  return null}
const eqOk2=(str,nums,a)=>eqOk(str,nums,a);
function segSvg(op,nums){const tot=op==='+'?'？':nums[0],p1=op==='+'?nums[0]:nums[1],p2=op==='+'?nums[1]:'？',W=260;
  const f=(op==='+'?nums[0]/(nums[0]+nums[1]):nums[1]/nums[0]),x=10+Math.max(.3,Math.min(.7,f))*240,tx=(a,b)=>(a+b)/2;
  const lab=(t,x0,y)=>`<text x="${x0}" y="${y}" text-anchor="middle" font-size="14" font-weight="700" fill="${t==='？'?'#e5484d':'currentColor'}">${t}</text>`;
  return `<svg viewBox="0 0 ${W} 72" class="seg" role="img" aria-label="線段圖"><g stroke="currentColor" stroke-width="2" fill="none"><path d="M10 22H250M10 16V28M250 16V28"/><path d="M10 46H250M10 40V52M${x} 40V52M250 40V52"/></g>${lab(tot,130,13)}${lab(p1,tx(10,x),68)}${lab(p2,tx(x,250),68)}</svg>`}
/* 應用題：可換情境；有 chk 時加「驗算」格；sg 時畫線段圖 */
const wpN0=MATH.wp.norm;
MATH.wp.norm=it=>{const r=wpN0(it);if(!r)return null;r.wk=WPT[one(it.wk)]?one(it.wk):'';r.sg=it.sg?1:0;r.chk=it.chk?1:0;return r};
MATH.wp.can=it=>!!(it.wk||it.tpl);
const wpG0=MATH.wp.gen;
MATH.wp.gen=it=>{if(it.wk){for(let t=0;t<30;t++){const o=wpGen(it.wk,{sg:it.sg});if(o){o.chk=it.chk;return o}}return it}return Object.assign({},wpG0(it),{sg:it.sg,chk:it.chk,wk:''})};
MATH.wp.units=(s,it)=>2+(it.chk?1:0);
const wpChk=(str,it)=>{const[a,b]=it.nums,c=it.a;return it.op==='+'?(eqOk(str,[c,b],a)||eqOk(str,[c,a],b)):it.op==='-'?(eqOk(str,[c,b],a)||eqOk(str,[a,c],b)):(c%b===0&&eqOk(str,[c,b],a))};
MATH.wp.ev=(sec,k,it,A)=>{const e=eqOk(A[k+'.e'],it.nums,it.a),an=digits(A[k+'.n'])===String(it.a)&&one(A[k+'.u']).replace(/\s/g,'')===it.u,v=it.chk?wpChk(A[k+'.v'],it):false;
  const mx=sec.pt*(2+(it.chk?1:0)),got=sec.pt*((e?1:0)+(an?1:0)+(v?1:0)),fl=!!(one(A[k+'.e'])||one(A[k+'.n'])||one(A[k+'.v']));return {got,max:mx,st:stOf(got,mx,fl),e,an,v}};
MATH.wp.render=(sec,si,it,ii,ck,k,no,r,M,A)=>{const o=MATH.wp.ev(sec,k,it,A);
  return `${no}${pe(it.q)}${it.sg?segSvg(it.op,it.nums):''}<div class="row">算式：<input class="pi ew" data-k="${k}.e" value="${pe(A[k+'.e']||'')}" ${ck?'readonly':''} placeholder="例：1250＋3588" autocomplete="off"> ${ck?(o.e?'✅':'❌'):''}</div><div class="row">答：${inp(k+'.n',A[k+'.n'],ck,'c4')} ${inp(k+'.u',A[k+'.u'],ck,'c1')} ${ck?(o.an?'✅':'❌'):''}</div>${it.chk?`<div class="row">驗算：<input class="pi ew" data-k="${k}.v" value="${pe(A[k+'.v']||'')}" ${ck?'readonly':''} placeholder="例：2838＋1212" autocomplete="off"> ${ck?(o.v?'✅':'❌'):''}</div>`:''}${M}${ck&&r.st!=='ok'?ansBox('算式：<b>'+pe(it.nums[0]+' '+(it.op==='-'?'−':it.op)+' '+it.nums[1])+'</b>　答：<b>'+it.a+' '+pe(it.u)+'</b>'+(it.chk?'<br>驗算：<b>'+pe(it.op==='+'?it.a+' − '+it.nums[1]+' ＝ '+it.nums[0]:it.op==='-'?it.a+' ＋ '+it.nums[1]+' ＝ '+it.nums[0]:it.a+' ÷ '+it.nums[1]+' ＝ '+it.nums[0])+'</b>':'')+'<br>'+vShow(it.op,it.nums[0],it.nums[1])):''}`};
/* 數線填空：標出的刻度要填數字 */
MATH.nl={name:'數線填空',
  norm:it=>{const st=MI(it.start||0),sp=MI(it.step),n=Math.min(17,Math.max(5,MI(it.n)||16)),bl=arr(it.blank).map(MI).filter(i=>i>=0&&i<n);if(!(st>=0)||!(sp>=1)||!bl.length)return null;const v=[...Array(n)].map((_,i)=>st+sp*i);if(v[n-1]>9999)return null;return {start:st,step:sp,n,blank:[...new Set(bl)].sort((x,y)=>x-y),v}},
  units:(s,it)=>it.blank.length,
  can:it=>true,
  gen:it=>{const sp=it.step===1?1:pick1([2,3,4,5,6,10].filter(x=>x!==it.step)),n=it.n,cnt=it.blank.length,pool=shuf2([...Array(n-1)].map((_,i)=>i+1)).slice(0,cnt).sort((a,b)=>a-b);return {start:0,step:sp,n,blank:pool}},
  ev:(sec,k,it,A)=>{let got=0,fl=0;it.blank.forEach((b,j)=>{const v=digits(A[k+'.'+j]);if(v)fl++;if(v===String(it.v[b]))got+=sec.pt});const max=sec.pt*it.blank.length;return {got,max,st:stOf(got,max,fl)}},
  render:(sec,si,it,ii,ck,k,no,r,M,A)=>`${no}<p class="sub2" style="margin:2px 0">□裡要填入哪一個數？（左右可以滑動）</p><div class="nlw">${it.v.map((x,i)=>{const j=it.blank.indexOf(i);return `<div class="nlp">${j<0?`<b>${x}</b>`:inp(k+'.'+j,A[k+'.'+j],ck,'c2')}<i></i></div>`}).join('')}</div>${M}${ck&&r.st!=='ok'?ansBox('正確答案：<b>'+it.blank.map(b=>it.v[b]).join('、')+'</b>（每一格加 '+it.step+'）'):''}`};
/* 組合題的 svg 圖（只收自己畫的圖） */
const svgOk=s=>{s=one(s);return /^<svg[\s\S]*<\/svg>$/.test(s)&&!/<script|on\w+\s*=|href|foreignObject|<style|<image/i.test(s)?s:''};

function npSecs(t,x){const r=normPaper({title:t,secs:x});if(!r||r.secs.length!==x.length){try{console.warn('npSecs 區段數不符',t)}catch(e){}return []}
  r.secs.forEach((sec,i)=>{if(sec.items.length!==x[i].items.length){try{console.warn('npSecs 題數不符',t,i,sec.items.length,x[i].items.length)}catch(e){}}const P=+x[i].P;if(P>0){let u=0;sec.items.forEach(it=>{u+=ppUnits[sec.k](sec,it)});if(u>0)sec.pt=P/u}});return r.secs}
