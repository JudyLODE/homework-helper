/*PRIV:M5:BEGIN 家用：數學習作第 1～4 單元綜合評量的「題型、題數、作答方式」（依使用者自己的習作照片整理；數字與文字每次都會換；公開版會移除這一段）*/
function makePrivM5(){
  const M=(t,pa)=>mkMx(t,pa),W=(k,o)=>Object.assign(wpGen(k),o||{});
  const rd=[
  {t:'第 20 回 第 1～4 單元綜合評量(1)',secs:npSecs('20',[
    {k:'mx',t:'一、填填看',d:'',P:21,items:[M('blkpv',{z:0,nopic:1}),M('shop')]},
    {k:'nl',t:'一、□裡要填入哪一個數？',d:'',P:9,items:[{start:0,step:20,n:8,blank:[4,5,7]}]},
    {k:'mx',t:'二、看表，想一想，回答問題',d:'',P:30,items:[M('cafe')]},
    {k:'circ',t:'三、買微波爐：圈出正確的金額',d:'',P:3,items:[{name:'微波爐',price:3565,kind:'money',d:[3,7,6,5]}]},
    {k:'wp',t:'三、兩臺微波爐相差多少元？先用算式記下來，再算算看',d:'',P:5,items:[W('sub')]},
    {k:'mx',t:'三、用四張數字卡排排看',d:'',P:16,items:[M('cardsum')]},
    {k:'mx',t:'三、哪些敘述是正確的？',d:'',P:16,items:[M('rope')]}])},
  {t:'第 21 回 第 1～4 單元綜合評量(2)',secs:npSecs('21',[
    {k:'seq',t:'一、按照數的順序填填看',d:'',P:20,items:[{start:9200,step:100,n:8,blank:[1,3,5,6,7]}]},
    {k:'mx',t:'二、認識不同長度的糖果，看圖回答問題',d:'',P:24,items:[M('robj',{v:'cmx',set:'candy'})]},
    {k:'mx',t:'三、幫忙做糖果，回答問題',d:'',P:48,items:[M('say2'),M('wpb',{k:'mul3'}),M('wpb',{k:'mul2'}),M('wpb',{k:'add'}),M('wpb',{k:'unk'}),M('wpb',{k:'sub'})]},
    {k:'mx',t:'四、牛奶糖訂單的金額，共幾元？',d:'',P:8,items:[M('bank')]}])}
  ];
  return rd.filter(z=>z.secs.length);
}
/*PRIV:M5:END*/
