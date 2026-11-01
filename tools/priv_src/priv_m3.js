/*PRIV:M3:BEGIN 家用：數學習作第3單元（長度）的「題型、題數、作答方式」（依使用者自己的習作照片整理；數字與文字每次都會換；公開版會移除這一段）*/
function makePrivM3(){
  const M=(t,pa)=>mkMx(t,pa);
  const rd=[
  {t:'第 11 回 認識毫米與長度換算',secs:npSecs('11',[
    {k:'ruler',t:'一、有多長？用尺量量看',d:'',P:16,items:[{name:'螞蟻',mm:8,o:'mm'},{name:'瓢蟲',mm:14,o:'mm'},{name:'名牌',mm:35},{name:'橡皮擦',mm:56}]},
    {k:'mx',t:'二、有多長？看圖填填看',d:'',P:33,items:[M('robj',{v:'mm',set:'candy'}),M('robj',{v:'cm',set:'tool'})]},
    {k:'mx',t:'三、填填看',d:'',P:15,items:[M('conv',{v:'c1'}),M('conv',{v:'c2'}),M('conv',{v:'c3'}),M('conv',{v:'c3'})]},
    {k:'mx',t:'四、填入＜、＝或＞',d:'',P:16,items:[M('cmpu'),M('cmpu'),M('cmpu'),M('cmpu')]},
    {k:'mx',t:'五、閱讀下文後，回答問題',d:'',P:20,items:[M('bee')]}])},
  {t:'第 12 回 長度的加減、數線',secs:npSecs('12',[
    {k:'nl',t:'一、□裡要填入哪一個數？填填看',d:'',P:24,items:[{start:0,step:1,n:16,blank:[3,6,7,10,12]},{start:0,step:4,n:16,blank:[4,7,10]}]},
    {k:'mx',t:'二、這是一條數線，看數線回答問題',d:'',P:28,items:[M('nlq',{v:1})]},
    {k:'mx',t:'三、算算看',d:'',P:6,items:[M('lenop',{op:'+'}),M('lenop',{op:'-'})]},
    {k:'mx',t:'四、做做看，再寫出答案',d:'',P:42,items:[M('lenwp',{k:'two'}),M('lenwp',{k:'stack'}),M('lenwp',{k:'rem'})]}])},
  {t:'第 13 回 第 3 單元複習(1)　基礎題',secs:npSecs('13',[
    {k:'ruler',t:'一、量一量，填填看',d:'',P:12,items:[{name:'50 元硬幣',mm:28},{name:'彩色筆',mm:52}]},
    {k:'mx',t:'二、有多長？看圖填填看',d:'',P:24,items:[M('robj',{v:'blk'})]},
    {k:'mx',t:'三、填填看',d:'',P:18,items:[M('unit',{u:'公分'}),M('unit',{u:'毫米'}),M('unit',{u:'公尺'}),M('conv',{v:'c3'}),M('conv',{v:'c2'})]},
    {k:'mx',t:'四、填入＜、＝或＞',d:'',P:12,items:[M('cmpu'),M('cmpu'),M('cmpu')]},
    {k:'mx',t:'五、這是一條數線，看數線回答問題',d:'',P:16,items:[M('nlq',{v:2})]},
    {k:'mx',t:'六、做做看，再寫出答案',d:'',P:18,items:[M('lenwp',{k:'tape'}),M('lenwp',{k:'grow'})]}])},
  {t:'第 14 回 第 3 單元複習(2)　進階題',secs:npSecs('14',[
    {k:'mx',t:'一、測量材料的長度，看圖填填看',d:'',P:30,items:[M('robj',{v:'cm',set:'bar'})]},
    {k:'mx',t:'二、測量身長，回答問題',d:'',P:16,items:[M('frog')]},
    {k:'mx',t:'三、回答下面問題',d:'',P:18,items:[M('lenwp',{k:'mix'})]},
    {k:'mx',t:'四、看數線，回答下面問題',d:'',P:36,items:[M('nlq',{v:3})]}])}
  ];
  return rd.filter(z=>z.secs.length);
}
/*PRIV:M3:END*/
