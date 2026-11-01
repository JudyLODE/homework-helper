/* ===== 第2單元（加減）模板 ===== */
const SYM={'+':'＋','-':'－','×':'×'};
MXG.eq=it=>{const pa=it.pa||{},op=pa.op||'+',f=pa.f||'r';
  for(let t=0;t<800;t++){let a,b,c;
    if(op==='×'){const la=pa.la||2;a=pa.z==='t'?rnd(1,9)*10:pa.z==='h'?rnd(2,9)*100:pa.m0?rnd(1,9)*100+rnd(1,9):rndLen(la);b=rnd(2,9);c=a*b;if(c>9999)continue;if(pa.c===1&&!hasCarry('×',a,b))continue;if(pa.c===0&&hasCarry('×',a,b))continue;return {s:`${a} × ${b} ＝ （ ）`,a:[String(c)]}}
    a=pa.th?rnd(2,9)*1000+(pa.th>1?rnd(0,9)*100:0):rndLen(pa.la||4);b=rndLen(pa.lb||4);
    if(op==='+'){c=a+b;if(c>9999)continue}else{if(a<=b)continue;c=a-b}
    if(pa.c===1&&!hasCarry(op,a,b))continue;if(pa.c===0&&hasCarry(op,a,b))continue;
    const S=SYM[op];
    if(f==='b')return {s:`${a} ${S} （ ） ＝ ${c}`,a:[String(b)]};
    if(f==='a')return {s:`（ ） ${S} ${b} ＝ ${c}`,a:[String(a)]};
    return {s:`${a} ${S} ${b} ＝ （ ）`,a:[String(c)]}}
  return it};
MXG.eqsel=it=>{const v=(it.pa||{}).v||'a',th=pick1(['水果','餅乾','飲料','麵包']);let st,good,bad,ans,u;
  if(v==='a'){const A=rnd(1000,2400),B=rnd(200,900);st=`動物園買了 ${A} 籃${th}，動物吃掉一些後，還剩下 ${B} 籃，動物吃掉多少籃${th}？`;good=`${A}－（ ）＝${B}`;bad=`${A}＋${B}＝（ ）`;ans=A-B;u='籃'}
  else if(v==='b'){const A=rnd(1500,4200),B=rnd(1200,5600),x=pick1(['滑板車','腳踏車','電動車']),y=pick1(['電動腳踏車','電動機車','變速車']);st=`一輛${x} ${A} 元，一輛${y}比${x}貴 ${B} 元，一輛${y}要多少元？`;good=`${A}＋${B}＝（ ）`;bad=`${B}－${A}＝（ ）`;ans=A+B;u='元'}
  else{const A=rnd(300,1200),B=rnd(2200,4800);st=`遊樂園裡有一些人，${A} 人離開後，還有 ${B} 人，遊樂園裡原來有幾人？`;good=`（ ）－${A}＝${B}`;bad=`${B}－${A}＝（ ）`;ans=A+B;u='人'}
  const f=Math.random()<.5;return {s:`${st}\n合適的算式是〔${f?bad+'｜'+good:good+'｜'+bad}〕\n答：（ ）${u}`,a:[String(ans)],c:[f?1:0]}};
MXG.walk=it=>{const w=pick1(['爺爺','奶奶','爸爸','媽媽']);for(let t=0;t<400;t++){const m=rnd(2600,4200),d=rnd(300,900),e=rnd(1500,3000),tot=m+m+d+e;if(Math.abs(tot-10000)<150||Math.abs(tot-10000)>1500)continue;
  return {h:`下表是${w}昨天走路運動紀錄表。`,tb:{head:['時間','早上','下午','晚上'],rows:[['步數（步）',String(m),'？',String(e)]]},s:`(1) ${w}下午走的步數比早上多 ${d} 步，${w}下午走了（ ）步？\n(2) ${w}昨天走的總步數有超過 10000 步嗎？〔有｜沒有〕`,a:[String(m+d)],c:[tot>10000?0:1]}}return it};
MXG.prize=it=>{const pool=shuf2([['玩具熊',3000,4200],['運動手環',3000,5200],['鉛筆',100,300],['籃球',900,1600],['保溫杯',600,1400],['書包',1800,2800]]).slice(0,4).map(x=>[x[0],Math.round(rnd(x[1],x[2])/10)*10]),[p1,p2]=shuf2(NAMES).slice(0,2),x=pool[1],y=pool[3],need=rnd(30,90)*10,rest=rnd(100,400);
  return {h:'下面是遊樂場彩券點數兌換對照表。',tb:{head:['獎品',...pool.map(p=>p[0])],rows:[['所需點數',...pool.map(p=>p[1]+' 點')]]},s:`(1) ${p1}有一些點數，還需要 ${need} 點才能換${x[0]}，${p1}有幾點？（ ）點\n(2) ${p2}換一個${y[0]}後，還剩下 ${rest} 點，${p2}原來有幾點？（ ）點`,a:[String(x[1]-need),String(y[1]+rest)]}};
function triSvg(h,p,s,d1,d2,d3){const t=(x,y,tx,an,sz)=>`<text x="${x}" y="${y}" text-anchor="${an||'middle'}" font-size="${sz||12}" fill="currentColor">${tx}</text>`;
  return `<svg viewBox="0 0 320 140" class="rl" role="img" aria-label="路線圖"><path d="M40 100L160 28L280 100Z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="40" cy="100" r="4" fill="currentColor"/><circle cx="160" cy="28" r="4" fill="currentColor"/><circle cx="280" cy="100" r="4" fill="currentColor"/>${t(40,122,h)}${t(160,16,p)}${t(280,122,s)}${t(80,56,d1+' 公尺','end')}${t(246,56,d2+' 公尺','start')}${t(160,136,d3+' 公尺')}</svg>`}
MXG.route=it=>{const [h,p,s]=pick1([['穎穎家','公園','便利商店'],['小安家','學校','文具店'],['阿宏家','市場','郵局'],['佳琪家','圖書館','早餐店']]);for(let t=0;t<300;t++){const d1=rnd(1200,3000),d2=rnd(900,2000),d3=rnd(Math.max(d1,d2)+200,d1+d2-300);if(!(d3>0)||d3>=d1+d2)continue;
  return {svg:triSvg(h,p,s,d1,d2,d3),h:'看圖做做看。',s:`1. 從${h}出發，經過${p}再到${s}，共走了（ ）公尺。\n2. 從${s}直接走回${h}，會比從${h}經過${p}到${s}少走（ ）公尺。`,a:[String(d1+d2),String(d1+d2-d3)]}}return it};
/* ===== 第3單元（長度）模板 ===== */
const cmmm=mm=>`${Math.floor(mm/10)} 公分 ${mm%10} 毫米`;
function robjSvg(objs){const mxm=Math.max(...objs.map(o=>o.mm)),cm=Math.min(14,Math.ceil(mxm/10)+1),W=cm*24+16,H0=objs.length*26+6,col=['#9fd6b5','#f6c177','#b7c9f0','#f4a9a8'];let t='',b='';
  objs.forEach((o,i)=>{const y=4+i*26,w=o.mm*2.4,inside=w>74;b+=`<rect x="8" y="${y}" width="${w}" height="18" rx="4" fill="${col[i%4]}" stroke="#345" stroke-width="1.5"/><text x="${inside?14:8+w+5}" y="${y+13}" font-size="11" fill="${inside?'#123':'currentColor'}">${pe(o.n)}</text><line x1="${8+w}" y1="${y+18}" x2="${8+w}" y2="${H0+2}" stroke="#889" stroke-dasharray="3 3"/>`});
  for(let i=0;i<=cm*10;i++){const x=8+i*2.4,h=i%10===0?14:i%5===0?10:6;t+=`<line x1="${x}" y1="0" x2="${x}" y2="${h}" stroke="#334" stroke-width="1"/>`;if(i%10===0)t+=`<text x="${x}" y="26" font-size="10" text-anchor="middle" fill="#334">${i/10}</text>`}
  return `<svg viewBox="0 0 ${W} ${H0+34}" class="rl" role="img" aria-label="尺和物品">${b}<rect x="0" y="${H0}" width="${W}" height="32" fill="#f4efe0" stroke="#334"/><g transform="translate(0,${H0})">${t}</g></svg>`}
const MMV=n=>{let x=rnd(n[0],n[1]);if(x%10===0)x+=rnd(1,3);return x};
const RPOOL={tool:['長尾夾','釘書針盒子','筆芯盒','橡皮擦','削鉛筆機','膠水','小剪刀','尺盒','便條紙','迴紋針盒'],bar:['松木條','柳樹條','竹條','藤條','塑膠條','鐵絲','麻繩','彩帶'],candy:['巧克力糖','棉花糖','牛奶糖','軟糖','拐杖糖','水果糖','太妃糖']};
const f2=mm=>[String(Math.floor(mm/10)),String(mm%10)];
MXG.robj=it=>{const v=(it.pa||{}).v||'cm';
  if(v==='blk'){const m=[rnd(5,9),rnd(10,19),rnd(25,40)];return {svg:robjSvg([{n:'正方形積木',mm:m[0]},{n:'長方形積木',mm:m[1]},{n:'箭頭形積木',mm:m[2]}]),h:'看圖填填看。',s:`1. 正方形積木和（ ）個 1 毫米一樣長，是（ ）毫米。\n2. 長方形積木長（ ）毫米，也可以說是（ ）公分（ ）毫米。\n3. 箭頭形積木長（ ）毫米，也可以說是（ ）公分（ ）毫米。`,a:[String(m[0]),String(m[0]),String(m[1]),...f2(m[1]),String(m[2]),...f2(m[2])]}}
  const set=(it.pa||{}).set||'tool',nm=shuf2(RPOOL[set]).slice(0,3);
  if(v==='mm'){const m=nm.map(()=>rnd(8,60));return {svg:robjSvg(nm.map((n,i)=>({n,mm:m[i]}))),h:'看圖填填看（尺上一小格是 1 毫米）。',s:`(1) ${nm[0]}和（ ）個 1 毫米一樣長，是（ ）毫米。\n(2) ${nm[1]}和（ ）個 1 毫米一樣長，是（ ）毫米。\n(3) ${nm[2]}的長是（ ）毫米。`,a:[String(m[0]),String(m[0]),String(m[1]),String(m[1]),String(m[2])]}}
  if(v==='cmx'){const m=nm.map(()=>MMV([22,125])),mxI=m.indexOf(Math.max(...m));if(m.filter(x=>x===m[mxI]).length>1)return MXG.robj(it);const f=shuf2([0,1,2]);
    return {svg:robjSvg(nm.map((n,i)=>({n,mm:m[i]}))),h:'看圖回答問題。',s:`1. ${nm[0]}的長是（ ）公分（ ）毫米。\n2. ${nm[1]}的長是（ ）公分（ ）毫米。\n3. ${nm[2]}的長是（ ）公分（ ）毫米，也可以說是（ ）毫米。\n4. 上面三種物品，哪一種的長度最長？〔${f.map(i=>nm[i]).join('｜')}〕`,a:[...f2(m[0]),...f2(m[1]),...f2(m[2]),String(m[2])],c:[f.indexOf(mxI)]}}
  const m=nm.map(()=>MMV([22,125]));return {svg:robjSvg(nm.map((n,i)=>({n,mm:m[i]}))),h:'看圖填填看。',s:nm.map((n,i)=>`(${i+1}) ${n}的長是（ ）公分（ ）毫米。`).join('\n'),a:m.flatMap(f2)}};
MXG.conv=it=>{const v=(it.pa||{}).v||'c3';
  if(v==='c1'){const n=rnd(1,9);return {s:`${n} 公分 ＝ （ ） 毫米`,a:[String(n*10)]}}
  if(v==='c2'){const mm=rnd(11,99);return {s:`${mm} 毫米 ＝ （ ） 公分 （ ） 毫米`,a:f2(mm)}}
  const a=rnd(1,9),b=rnd(1,9);return {s:`${a} 公分 ${b} 毫米 ＝ （ ） 毫米`,a:[String(a*10+b)]}};
MXG.cmpu=it=>{const fm=(mm,k)=>k===0?`${mm} 毫米`:k===1?`${mm/10} 公分`:cmmm(mm);
  for(let t=0;t<600;t++){const o=rnd(0,2),L=rnd(30,990);let R=o===1?L:o===0?L+rnd(5,90):L-rnd(5,90);if(R<10)continue;const kl=rnd(0,2),kr=rnd(0,2);if(kl===kr)continue;if((kl===1&&L%10)||(kr===1&&R%10))continue;
    return {s:`${fm(L,kl)} 〔＜｜＝｜＞〕 ${fm(R,kr)}`,c:[L<R?0:L===R?1:2],a:[]}}return it};
const UP=[['鉛筆盒的長度','公分',15,25],['鉛筆的長度','毫米',120,180],['學校操場的跑道長','公尺',200,400],['橡皮擦的長度','毫米',40,60],['課桌的寬度','公分',55,70],['教室的長度','公尺',8,12],['迴紋針的長度','公分',3,4],['游泳池的長度','公尺',25,50],['螞蟻的身長','毫米',3,9],['彩色筆的長度','公分',12,18],['籃球場的長度','公尺',26,30],['吸管的粗細','毫米',5,8],['書包的高度','公分',35,45],['公車的長度','公尺',9,12]];
MXG.unit=it=>{const u=(it.pa||{}).u||'公分',x=pick1(UP.filter(p=>p[1]===u)),n=rnd(x[2],x[3]),o=['毫米','公分','公尺'];return {s:`${x[0]}是 ${n} 〔毫米｜公分｜公尺〕。`,a:[],c:[o.indexOf(u)]}};
MXG.bee=it=>{const T=pick1([['蜂后','工蜂','雄蜂','蜜蜂的社會跟人類很相似，牠們是一種會分工合作、各有自己負責工作的社會性昆蟲。下表是研究人員幫不同的蜜蜂測量出的身長紀錄表。'],['蟻后','工蟻','雄蟻','螞蟻是群居的昆蟲，每一個蟻巢裡都有蟻后、工蟻和雄蟻，大家分工合作。下表是研究人員幫不同的螞蟻測量出的身長紀錄表。'],['蝶后','工蝶','雄蝶','小朋友在昆蟲館裡觀察到三種身形不同的蝴蝶。下表是館員幫不同的蝴蝶測量出的身長紀錄表。']]),B=rnd(11,35),A=B+3,[x,y,z]=[T[0],T[1],T[2]];
  return {ctx:T[3],tb:{head:['名稱',x,y,z],rows:[['身長',A+' 毫米',Math.floor(B/10)+' 公分 '+B%10+' 毫米','？']]},s:`1. ${x}的身長是 ${A} 毫米，也可以說是（ ）公分（ ）毫米。\n2. ${y}的身長是 ${Math.floor(B/10)} 公分 ${B%10} 毫米，也可以說是（ ）毫米。\n3. ${z}的身長介於${x}與${y}之間，${z}的身長可能是（ ）毫米或（ ）毫米。`,a:[...f2(A),String(B),(B+1)+'|'+(B+2),(B+1)+'|'+(B+2)],uq:[[3,4]]}};
MXG.lenop=it=>{const op=(it.pa||{}).op||'+';for(let t=0;t<200;t++){const a1=rnd(2,9),b1=rnd(1,8),a2=rnd(1,6),b2=rnd(1,8);let r;
  if(op==='+'){if(b1+b2>9)continue;r=[a1+a2,b1+b2]}else{if(a1<=a2||b1<b2)continue;r=[a1-a2,b1-b2]}
  return {s:`${a1} 公分 ${b1} 毫米 ${SYM[op]} ${a2} 公分 ${b2} 毫米 ＝ （ ） 公分 （ ） 毫米`,a:r.map(String)}}return it};
const LNAME=[['水彩筆','毛筆'],['鉛筆','原子筆'],['紅絲帶','藍絲帶'],['長尺','短尺']];
MXG.lenwp=it=>{const k=(it.pa||{}).k||'two';
  if(k==='two'){const [p,q]=pick1(LNAME),x=rnd(140,230),y=rnd(100,x-15);return {h:`${p}長 ${cmmm(x)}，${q}長 ${cmmm(y)}。`,s:`(1) 將兩個連接在一起，長是（ ）公分（ ）毫米？\n(2) ${p}比${q}長（ ）公分（ ）毫米？`,a:[...f2(x+y),...f2(x-y)]}}
  if(k==='stack'){const x=pick1(['面紙','積木盒','書','餅乾盒']),h=rnd(50,140);return {h:`一個${x}高 ${cmmm(h)}。`,s:`(1) 將 2 個${x}疊在一起，高是（ ）公分（ ）毫米？\n(2) 接第 (1) 題，再疊 1 個${x}，高是（ ）公分（ ）毫米？`,a:[...f2(2*h),...f2(3*h)]}}
  if(k==='rem'){const T=rnd(30,60),a=rnd(100,170),b=rnd(90,160);return {h:`媽媽織一條 ${T} 公分的小熊圍巾。`,s:`(1) 第一天，媽媽織了 ${cmmm(a)}，還剩下（ ）公分（ ）毫米要織？\n(2) 第二天，媽媽又織了 ${cmmm(b)}，還剩下（ ）公分（ ）毫米就織完？`,a:[...f2(T*10-a),...f2(T*10-a-b)]}}
  if(k==='tape'){const a=rnd(300,480),b=rnd(150,260);return {h:'',s:`一條緞帶包裝禮物用掉 ${cmmm(a)} 後，還剩下 ${cmmm(b)}，這條緞帶原來有（ ）公分（ ）毫米長？`,a:f2(a+b)}}
  if(k==='grow'){const a=rnd(450,560),b=rnd(780,880);return {h:'',s:`弟弟出生時身高 ${cmmm(a)}，現在身高 ${cmmm(b)}，弟弟長高了（ ）公分（ ）毫米？`,a:f2(b-a)}}
  const [p,q]=pick1([['玉米','胡蘿蔔'],['香蕉','小黃瓜'],['蘆筍','茄子']]),a=rnd(150,230),b=rnd(100,a-15);return {h:`小光到馬區幫忙餵食，他拿到的${p}長 ${cmmm(a)}，${q}長 ${b} 毫米。`,s:`(1) 把${p}和${q}接在一起，是（ ）公分（ ）毫米？\n(2) ${p}和${q}的長相差了（ ）公分（ ）毫米？`,a:[...f2(a+b),...f2(a-b)]}};
MXG.frog=it=>{const x=pick1(['樹蛙','蝸牛','小烏龜']),dad=rnd(36,52),mom=rnd(40,60);if(dad===mom)return MXG.frog(it);const o=shuf2(['公尺','公分','毫米']),ci=o.indexOf('公尺'),cw=dad>mom?0:1;
  return {s:`1. ${x}的大小約和小光掌心一樣大，要測量${x}的身長，使用下面哪一個單位比較不合適？〔${o.join('｜')}〕\n2. ${x}爸爸身長是 ${dad} 毫米，也可以說是（ ）公分（ ）毫米。\n3. ${x}媽媽身長是 ${cmmm(mom)}，也可以說是（ ）毫米。\n4. 接第 2、3 題，誰的身長比較長？〔${x}爸爸｜${x}媽媽｜無法判斷〕`,a:[...f2(dad),String(mom)],c:[ci,cw]}};
/* ===== 數線圖與題組 ===== */
const NLM=[['小烏龜','🐢'],['小松鼠','🐿️'],['青菜','🥬'],['兔子','🐰'],['小熊','🐻'],['蘑菇','🍄'],['小鳥','🐦'],['蘋果','🍎'],['大象','🐘'],['小貓','🐱'],['小狗','🐶'],['青蛙','🐸']];
function nlSvg(N,marks){const W=N*24+40;let s=`<line x1="14" y1="66" x2="${W-14}" y2="66" stroke="currentColor" stroke-width="2"/><text x="2" y="62" font-size="10" fill="currentColor">左</text><text x="${W-12}" y="62" font-size="10" fill="currentColor">右</text>`;
  for(let i=0;i<=N;i++){const x=20+i*24;s+=`<line x1="${x}" y1="62" x2="${x}" y2="70" stroke="currentColor"/><text x="${x}" y="84" text-anchor="middle" font-size="11" fill="currentColor">${i}</text>`}
  marks.forEach(m=>{const x=20+m.p*24;s+=`<text x="${x}" y="14" text-anchor="middle" font-size="11" fill="currentColor">${m.n}</text><text x="${x}" y="40" text-anchor="middle" font-size="22">${m.e}</text><line x1="${x}" y1="44" x2="${x}" y2="62" stroke="#889" stroke-dasharray="2 3"/>`});
  return `<svg viewBox="0 0 ${W} 92" class="rl" role="img" aria-label="數線圖">${s}</svg>`}
MXG.nlq=it=>{const v=+(it.pa||{}).v||1;
  for(let t=0;t<400;t++){const nm=shuf2(NLM).slice(0,4),N=v===1?14:16;let ps,s,a=[],c=[];
    if(v===1){const pB=rnd(3,5),pC=rnd(7,9),pD=rnd(11,13),aa=rnd(3,6),d=rnd(2,4),np=pC+d;if(np===pD||np>N)continue;const e=rnd(3,pD-3),f=rnd(pB+3,N-1);ps=[0,pB,pC,pD];
      s=`1. ${nm[0][0]}從位置 0 向右出發，走了 ${aa} 格，會停在位置（ ）。\n2. ${nm[0][0]}從位置 0 出發，走到${nm[2][0]}處，是走了（ ）格。\n3. 將${nm[2][0]}向右移 ${d} 格，會停在位置（ ）。\n4. 接第 3 題，${nm[3][0]}從位置 ${pD} 要跳到${nm[2][0]}的位置，是往〔左｜右〕跳（ ）格。\n5. ${nm[3][0]}從位置 ${pD} 往左跳到位置 ${e}，是跳了幾格？寫出算式算算看。\n算式：（ ）－（ ）＝（ ）\n6. ${nm[1][0]}從位置 ${pB} 往右跳到位置 ${f}，是跳了多少格？寫出算式算算看。\n算式：（ ）－（ ）＝（ ）`;
      a=[aa,pC,np,Math.abs(pD-np),pD,e,pD-e,f,pB,f-pB].map(String);c=[pD>np?0:1]}
    else if(v===2){const pU=rnd(12,15),pY=rnd(2,5),pZ=rnd(9,11),aa=rnd(2,4),tt=rnd(pY+3,pY+7),d=rnd(3,5),e=rnd(4,7),f=rnd(2,4);if(pU-e+f>N||pU-e<0)continue;ps=[0,pY,pZ,pU];
      s=`1. ${nm[0][0]}從位置 0 向右出發，走了 ${aa} 格，會停在位置（ ）。\n2. ${nm[1][0]}從位置 ${pY} 向右出發，走到位置 ${tt}，是走了（ ）格。\n3. ${nm[2][0]}向左移動 ${d} 格，會到位置（ ）。\n4. ${nm[3][0]}從位置 ${pU} 先往左走 ${e} 格，再往右走 ${f} 格，會停在位置（ ）。`;
      a=[aa,tt-pY,pZ-d,pU-e+f].map(String)}
    else{const pY=rnd(10,13),pV=rnd(4,7),pU=rnd(13,15),aa=rnd(4,7),e=rnd(3,6),g=rnd(5,9),p5=rnd(4,7),p6=rnd(8,11),q6=rnd(3,p6-2),h1=pick1(['保育員康康','保育員莉莉','管理員小華']);if(p5+g>N)continue;ps=[0,pV,pY,pU];
      s=`1. ${nm[0][0]}從位置 0 向右出發，走了 ${aa} 格，會停在位置（ ）。\n2. ${nm[2][0]}的位置距離位置 0 有（ ）格。\n3. ${nm[3][0]}從位置 ${pU} 出發，向左走了 ${e} 格，會走到位置多少？\n算式：（ ）－（ ）＝（ ）\n4. ${nm[1][0]}走到${nm[2][0]}處，是向右走了幾格？\n算式：（ ）－（ ）＝（ ）\n5. ${h1}從位置 ${p5} 往右走 ${g} 格，會走到位置多少？\n算式：（ ）＋（ ）＝（ ）\n6. ${h1}從位置 ${p6} 往左走到位置 ${q6}，是走了多少格？\n算式：（ ）－（ ）＝（ ）`;
      a=[aa,pY,pU,e,pU-e,pY,pV,pY-pV,p5,g,p5+g,p6,q6,p6-q6].map(String)}
    return {svg:nlSvg(N,nm.map((m,i)=>({n:m[0],e:m[1],p:ps[i]}))),h:'這是一條數線，看數線回答問題。',s,a,c}}
  return it};
