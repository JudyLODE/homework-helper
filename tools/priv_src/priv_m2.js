/*PRIV:M2:BEGIN 家用：數學習作第2單元（加減）的「題型、題數、作答方式」（依使用者自己的習作照片整理；數字與文字每次都會換；公開版會移除這一段）*/
function makePrivM2(){
  const M=(t,pa)=>mkMx(t,pa),W=(k,o)=>Object.assign(wpGen(k),o||{}),E=(pa)=>M('eq',pa);
  const rd=[
  {t:'第 6 回 10000 以內的加法',secs:npSecs('6',[
    {k:'mx',t:'一、寫成直式算算看',d:'',P:40,items:[{la:3,lb:4},{la:4,lb:4},{la:3,lb:4},{la:4,lb:4,c:1},{la:4,lb:4},{la:4,lb:4},{la:4,lb:4,c:1},{la:4,lb:4,c:1}].map(p=>E(Object.assign({op:'+'},p)))},
    {k:'wp',t:'二、先用算式記下來，再用直式算算看',d:'',P:48,items:[W('add'),W('add'),W('add'),W('add'),W('add'),W('add')]},
    {k:'mx',t:'三、看表回答問題',d:'',P:12,items:[M('walk')]}])},
  {t:'第 7 回 10000 以內的減法',secs:npSecs('7',[
    {k:'mx',t:'一、寫成直式算算看',d:'',P:40,items:[{la:4,lb:4},{la:4,lb:4,c:1},{la:4,lb:4},{la:4,lb:4,c:1},{la:4,lb:4,c:1},{la:4,lb:4,c:1},{la:4,lb:3,c:1},{la:4,lb:4,c:1}].map(p=>E(Object.assign({op:'-'},p)))},
    {k:'wp',t:'二、先用算式記下來，再用直式算算看',d:'',P:48,items:[W('sub'),W('sub'),W('sub'),W('sub'),W('sub'),W('sub')]},
    {k:'wp',t:'三、先用算式記下來，再用直式算算看，並驗算',d:'',P:12,items:[W('sub',{chk:1})]}])},
  {t:'第 8 回 加與減',secs:npSecs('8',[
    {k:'mx',t:'一、算算看，（ ）裡的數是多少？',d:'',P:24,items:[E({op:'+',f:'b'}),E({op:'+',f:'a'}),E({op:'-',f:'b',th:1}),E({op:'-',f:'a'})]},
    {k:'wp',t:'二、先用算式記下來，再用直式算算看（看線段圖）',d:'',P:28,items:[W('unk',{sg:1}),W('orig',{sg:1})]},
    {k:'wp',t:'三、先用算式記下來，再用直式做做看',d:'',P:38,items:[W('orig',{sg:1}),W('unk'),W('orig'),W('unk')]},
    {k:'mx',t:'三、先用算式記下來，再用直式做做看（看表）',d:'',P:10,items:[M('prize')]}])},
  {t:'第 9 回 第 2 單元複習(1)　基礎題',secs:npSecs('9',[
    {k:'mx',t:'一、算算看，（ ）裡的數是多少？',d:'',P:48,items:[E({op:'+',f:'r',la:4,lb:4}),E({op:'+',f:'r',la:3,lb:4}),E({op:'-',f:'r',la:4,lb:4}),E({op:'-',f:'r',la:4,lb:4}),E({op:'+',f:'b'}),E({op:'+',f:'a'}),E({op:'-',f:'a'}),E({op:'-',f:'b',th:1})]},
    {k:'wp',t:'二、先用算式記下來，再用直式算算看',d:'',P:32,items:[W('add'),W('add'),W('sub'),W('sub')]},
    {k:'wp',t:'三、先用算式記下來，再用直式算算看，並驗算',d:'',P:20,items:[W('sub',{chk:1}),W('sub',{chk:1})]}])},
  {t:'第 10 回 第 2 單元複習(2)　進階題',secs:npSecs('10',[
    {k:'mx',t:'一、算算看，（ ）裡的數是多少？',d:'',P:20,items:[E({op:'+',f:'b',th:1}),E({op:'+',f:'a'}),E({op:'-',f:'a'}),E({op:'-',f:'b'})]},
    {k:'mx',t:'二、把合適的算式選出來，並算出答案',d:'',P:30,items:[M('eqsel',{v:'a'}),M('eqsel',{v:'b'}),M('eqsel',{v:'c'})]},
    {k:'wp',t:'三、先用算式記下來，再用直式算算看',d:'',P:36,items:[W('add'),W('add'),W('sub'),W('sub')]},
    {k:'mx',t:'四、看圖做做看',d:'',P:14,items:[M('route')]}])}
  ];
  return rd.filter(z=>z.secs.length);
}
/*PRIV:M2:END*/
