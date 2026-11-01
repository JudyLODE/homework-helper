/* ===== 考卷出題：選科目、選課程範圍 → 出一份 100 分的考卷（電子作答／列印試卷／解答） ===== */
const EXBAD=['circ','lkm','draw'];
const EXN=['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五'];
const EXST={mid:{n:'期中風格',u:44,big:8},end:{n:'期末風格',u:58,big:10}};
const isEx=s=>!!(s&&s.pp&&s.pp.ex);
function exLessons(sub){return SEC.map((s,i)=>({s,i})).filter(x=>!x.s.del&&!isEx(x.s)&&sk(x.s)===sub)}
function exHasTpl(L){return !!(L.pp&&L.pp.z&&L.pp.z.some(z=>z.secs.some(sec=>MREGEN(sec.k,sec)&&!EXBAD.includes(sec.k))))}
const exUnits=sec=>sec.pt>0?Math.round(ppMax(sec)/sec.pt):0;
function exPoints(secs){const U=secs.reduce((a,s)=>a+exUnits(s),0)||1,raw=secs.map(s=>100*exUnits(s)/U),fl=raw.map(Math.floor);let rem=100-fl.reduce((a,b)=>a+b,0);
  raw.map((x,i)=>[x-fl[i],i]).sort((a,b)=>b[0]-a[0]).forEach(([,i])=>{if(rem>0){fl[i]++;rem--}});
  secs.forEach((s,i)=>{const u=exUnits(s);s.sp=fl[i];s.pt=u?fl[i]/u:s.pt;s.t=EXN[i]+'、'+String(s.t||'').replace(/^[一二三四五六七八九十]+[、.．]\s*/,'')});return secs}
/* 數學：從選到的課程的習作題型範本，重新出題（數字、文字都是新的） */
function exMath(idxs,style){
  const T=EXST[style]||EXST.mid;
  const cand=idxs.map(i=>{const L=SEC[i],out=[];((L.pp&&L.pp.z)||[]).forEach(z=>z.secs.forEach(sec=>{
    if(EXBAD.includes(sec.k)||!MREGEN(sec.k,sec))return;
    const items=sec.items.filter(it=>!(sec.k==='mx'&&it.dp!==undefined));if(!items.length)return;
    const s2=Object.assign({},sec,{items}),u=items.reduce((a,it)=>a+ppUnits[sec.k](sec,it),0);if(u<1||u>16)return;out.push({sec:s2,u,z:z.t,L:i})}));return shuf2(out)}).filter(a=>a.length);
  if(!cand.length)return [];
  const pick=[],used=new Set();let U=0,guard=0;
  while(U<T.u&&guard++<60){let moved=false;
    for(const c of cand){if(U>=T.u&&pick.length>=Math.min(cand.length,T.big))break;
      const ks=new Set(pick.map(p=>p.sec.k)),y=c.find(v=>!used.has(v)&&!ks.has(v.sec.k))||c.find(v=>!used.has(v));
      if(!y||(U+y.u>T.u*1.35&&pick.length>=cand.length))continue;used.add(y);pick.push(y);U+=y.u;moved=true}
    if(!moved)break}
  pick.sort((a,b)=>a.L-b.L);
  return exPoints(pick.map(p=>ppRegenSec(p.sec)));
}
/* 其他科目：AI 讀課程內容出題 */
function exDigest(idxs){return idxs.map(i=>{const s=SEC[i],o={課程:s.t};
  if(s.info&&s.info.r)o.重點=s.info.r.slice(0,14).map(x=>x[0]+(x[1]?'（'+x[1]+'）':''));
  if(s.w&&s.w.length)o.詞語=s.w.slice(0,30).map(x=>x[0]+'＝'+x[1]);
  if(s.d&&s.d.length)o.題目=s.d.slice(0,12).map(x=>x[0]+' → '+x[2]);
  if(s.tf&&s.tf.length)o.是非=s.tf.slice(0,8).map(x=>x[0]+' → '+(x[1]?'對':'錯'));
  if(s.full&&s.full.p)o.課文=s.full.p.join('\n').slice(0,1800);
  if(s.pp){const sec=[];[...(s.pp.o||[]),...(s.pp.z||[]).flatMap(z=>z.secs)].slice(0,8).forEach(x=>{sec.push(x.t+'：'+(x.items||[]).slice(0,2).map(it=>it.s||it.q||it.p||'').join('／'))});if(sec.length)o.習作=sec}
  return JSON.stringify(o).slice(0,3600)}).join('\n')}
const EXPROMPT=(sub,idxs,style)=>`你是台灣國小三年級${SUB[sub].n}老師，要依下面「學生學過的課程內容」出一份學校${EXST[style].n}的考卷，只能考這些內容，不可超出範圍；用繁體中文（台灣用語）。
${sub==='cn'?'國語答案以教育部《重編國語辭典修訂本》為準；不出計算、筆畫、口語跟讀題。':''}
共 ${EXST[style].big} 個大題左右，題型要像學校考試（選擇題、○×題、填空、連連看、造句、選填詞語、重組語句等），難度由易到難，每個大題 3～8 題，答案必須能從課程內容確定。
只輸出 JSON：{"secs":[{"k":題型,"t":"大題標題","d":"作答說明","pt":每題分數,"items":[…]}]}
題型 k 與 items 格式：
mc 選擇題：{"q":"題目","o":["選項1","選項2","選項3"],"a":正確選項的號碼(從0開始)}
tfx ○×題：{"s":"敘述","a":true或false}
fill 填空：{"s":"句子，空格用（ ）","a":["答案1",…]}（空格數＝答案數）
num 填數字：{"q":"題目","a":"數字"}
bank 選填詞語（大題要有 "bank":["詞1","詞2",…]）：{"s":"句子，空格用（ ）","a":["答案",…]}
link 連一連：{"l":"左邊","r":"右邊"}（同一大題至少 3 組）
ord 語句重組：{"w":["詞1","詞2","詞3",…]}（詞語依正確順序）
sent 造句：{"kw":"詞語","q":"造句要求"}
課程內容：
${exDigest(idxs)}`;
async function exAI(sub,idxs,style){
  const ctl=new AbortController(),tm=setTimeout(()=>ctl.abort(),270000);
  let raw;try{raw=await aiCall(EXPROMPT(sub,idxs,style),[],ctl,tm)}finally{clearTimeout(tm)}
  const x=arr(raw).find(o=>o&&o.secs!==undefined)||arr(raw)[0]||raw;
  const p=x&&Array.isArray(x.secs)?normPaper({title:'考卷',secs:x.secs}):null;
  if(!p||!p.secs.length)throw '這次 AI 沒有整理出可用的題目，請再按一次「出題」。';
  p.secs.forEach(s=>{if(s.k==='link'&&s.items.length<2)s.items=[]});
  const secs=p.secs.filter(s=>s.items.length&&ppMax(s)>0);if(!secs.length)throw '這次 AI 沒有整理出可用的題目，請再按一次「出題」。';
  return exPoints(secs);
}
function exSave(sub,secs,idxs,style){
  const d=new Date(),stamp=iso()+' '+String(d.getHours()).padStart(2,'0')+String(d.getMinutes()).padStart(2,'0'),t=`🧾 ${SUB[sub].n}考卷（${EXST[style].n}）${stamp}`;
  const L={date:iso(),sub,lang:'zh',t,en:'範圍：'+idxs.map(i=>SEC[i].t).join('、').slice(0,60),pg:'',ic:'🧾',c:SUB[sub].c,w:[],d:[],tf:[],calc:[],so:[],mt:[],parent:[],info:null,custom:1,m:['paper'],
    pp:{title:t,o:[],h:[],q:[],z:[{t:'考卷',secs}],src:1,vf:1,map:1,zp:1,zl:'考卷',ex:1,exs:style,exr:idxs.map(i=>SEC[i].t)}};
  SEC.push(L);LS.push(L);saveLS();return L}
function exam(){
  const X=S.ex=S.ex||{sub:'math',sel:[],style:'mid'},ls=exLessons(X.sub),saved=SEC.map((s,i)=>({s,i})).filter(x=>!x.s.del&&isEx(x.s)&&sk(x.s)===X.sub).reverse();
  const ok=x=>X.sub!=='math'||exHasTpl(x.s);
  const list=ls.length?ls.map(x=>`<button class="go ${X.sel.includes(x.i)?'':'alt'}" style="margin:0 0 6px;text-align:left;${ok(x)?'':'opacity:.5'}" data-a="ex_t" data-v="${x.i}" ${ok(x)?'':'disabled'}>${X.sel.includes(x.i)?'☑':'☐'} ${pe(x.s.t)}${ok(x)?'':'<span class="sub2">　（這課還沒有習作題型，暫時不能出題）</span>'}</button>`).join(''):`<p class="sub">這一科還沒有課程。請先到首頁「建立今天的作業課程」上傳。</p>`;
  const sv=saved.map(x=>`<div class="pq" style="margin:0 0 8px"><b>${pe(x.s.t)}</b><p class="sub2" style="margin:2px 0 6px">${pe(x.s.en||'')}</p><div style="display:flex;gap:6px;flex-wrap:wrap"><button class="go alt" style="margin:0;flex:1" data-a="ex_do" data-v="${x.i}">📝 電子作答</button><button class="go alt" style="margin:0;flex:1" data-a="ex_pq" data-v="${x.i}">🖨️ 試卷</button><button class="go alt" style="margin:0;flex:1" data-a="ex_pa" data-v="${x.i}">✅ 解答</button><button class="go alt" style="margin:0" data-a="ex_del" data-v="${x.i}">${S.exd===x.i?'再按一次刪除':'🗑'}</button></div></div>`).join('');
  return `${back('home','回到首頁')}<h2>🧾 考卷出題</h2>
  <p class="sub">選科目、勾選考試範圍，按「出題」，會依學過的課程重新出一份 100 分的考卷；可以電子作答，也可以印成 A4 黑白雙面的紙本試卷，解答在另一個按鈕。</p>
  <h3 class="pt">① 選科目</h3><div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px">${Object.keys(SUB).map(k=>`<button class="go ${X.sub===k?'':'alt'}" style="margin:0;flex:1;min-width:5.5em" data-a="ex_sub" data-v="${k}">${SUB[k].ic} ${SUB[k].n}</button>`).join('')}</div>
  <h3 class="pt">② 勾選考試範圍（課程）</h3>${list}
  <h3 class="pt">③ 考卷風格</h3><div style="display:flex;gap:6px;margin-bottom:10px">${Object.keys(EXST).map(k=>`<button class="go ${X.style===k?'':'alt'}" style="margin:0;flex:1" data-a="ex_st" data-v="${k}">${EXST[k].n}</button>`).join('')}</div>
  ${S.exMsg?`<p class="fb ${/^❌/.test(S.exMsg)?'oops':'good'}">${pe(S.exMsg)}</p>`:''}
  <button class="go" data-a="ex_go" ${X.sel.length&&!S.exBusy?'':'disabled style="opacity:.5"'}>${S.exBusy?'⏳ 出題中，請稍等…':'✨ 出題（總分 100 分）'}</button>
  ${X.sub!=='math'?'<p class="sub2">國語、英文、自然、社會由 AI 依課程內容出題，需要先在「功能設定」填好 AI 服務。數學用程式出題，答案由程式計算。</p>':''}
  <h3 class="pt" style="margin-top:18px">我的考卷${saved.length?'（'+saved.length+'）':''}</h3>${sv||'<p class="sub">還沒有出過考卷。</p>'}`;
}
function exSheet(les,mode){
  const secs=les.pp.z[0].secs,sv=[S.pp,S.s];S.s=SEC.indexOf(les);S.pp={ver:'z0',i:0,a:{},ck:{},pc:{},perm:{},sum:0};let h='';
  try{secs.forEach((sec,si)=>{const ck=mode==='a';if(ck)S.pp.ck['z0'+si]=1;
    const body=sec.k==='tbl'?tblHtml(sec):sec.k==='txt'?sec.items.map(it=>`<p class="pq" style="white-space:pre-wrap">${pe(it.p)}</p>`).join(''):sec.k==='link'?linkHtml(sec,si,ck):sec.items.map((it,ii)=>ppItem(sec,si,it,ii,ck)).join('');
    h+=`<section class="exs"><h3>${pe(sec.t)}<span class="exp">（${sec.sp||0} 分）</span></h3>${sec.d?`<p class="exd">${pe(noPts(sec.d))}</p>`:''}${sec.bank?`<div class="bankbox"><b>詞語框</b>：${sec.bank.map(x=>`<span>${pe(x)}</span>`).join('')}</div>`:''}${sec.note?`<p class="note">${pe(sec.note)}</p>`:''}<div class="pitems">${body}</div></section>`})}
  finally{S.pp=sv[0];S.s=sv[1]}
  return h}
function examprint(){
  const les=SEC[S.exi],m=S.exm;if(!les||!isEx(les))return `${back('exam','回到考卷出題')}<p>找不到這份考卷。</p>`;
  const sub=SUB[sk(les)].n,st=EXST[les.pp.exs]||EXST.mid;
  return `<div class="noprint">${back('exam','回到考卷出題')}<h2>${m==='a'?'✅ 解答':'🖨️ 列印試卷'}</h2><p class="sub">按「列印」，紙張選 <b>A4</b>、<b>黑白</b>、<b>雙面列印（長邊翻頁）</b>。${m==='a'?'解答頁不要發給學生。':''}</p><button class="go" data-a="ex_print">🖨️ 列印</button></div>
  <div class="sheet ${m==='a'?'ansmode':''}"><div class="exh"><h1>${pe(sub)}科　${st.n}　${m==='a'?'解答':'試卷'}</h1><div class="exf">班級：＿＿＿＿　座號：＿＿＿＿　姓名：＿＿＿＿＿＿＿＿　得分：＿＿＿＿ / 100</div><div class="exr">考試範圍：${pe((les.pp.exr||[]).join('、'))}</div></div>${exSheet(les,m)}</div>`;
}
async function exClick(b){
  const a=b.dataset.a,v=b.dataset.v,X=S.ex=S.ex||{sub:'math',sel:[],style:'mid'};
  if(a==='ex_sub'){X.sub=v;X.sel=[];S.exMsg=''}
  else if(a==='ex_t'){const i=+v,j=X.sel.indexOf(i);if(j>=0)X.sel.splice(j,1);else X.sel.push(i);X.sel.sort((p,q)=>p-q)}
  else if(a==='ex_st'){X.style=v}
  else if(a==='ex_go'){
    if(S.exBusy||!X.sel.length)return;S.exMsg='';
    try{
      let secs;
      if(X.sub==='math'){secs=exMath(X.sel,X.style);if(!secs.length)throw '選到的課程還沒有可以出題的習作題型。'}
      else{if(!AI.url&&!SMP)throw '還沒設定 AI 服務，請到首頁「功能設定」的家長專區填寫。';S.exBusy=1;render();secs=await exAI(X.sub,X.sel,X.style)}
      const L=exSave(X.sub,secs,X.sel,X.style);S.exMsg='✅ 已出好「'+L.t+'」，共 '+secs.length+' 個大題，總分 100 分。下面可以電子作答、列印試卷、看解答。'}
    catch(e){S.exMsg='❌ '+(typeof e==='string'?e:aiErr(e))}
    S.exBusy=0}
  else if(a==='ex_do'){S.s=+v;S.v='sec';ppStart('z0');window.scrollTo(0,0);return}
  else if(a==='ex_pq'||a==='ex_pa'){S.exi=+v;S.exm=a==='ex_pa'?'a':'q';S.v='examprint';window.scrollTo(0,0)}
  else if(a==='ex_del'){const i=+v;if(S.exd!==i){S.exd=i}else{SEC[i].del=1;S.exd=-1;saveLS()}}
  else if(a==='ex_print'){try{window.print()}catch(e){}return}
  render();
}
