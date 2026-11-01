/*PRIV:M4:BEGIN 家用：數學習作第4單元（乘法）的「題型、題數、作答方式」（依使用者自己的習作照片整理；數字與文字每次都會換；公開版會移除這一段）*/
function makePrivM4(){
  const M=(t,pa)=>mkMx(t,pa),W=(k,o)=>Object.assign(wpGen(k),o||{}),X=(pa)=>M('eq',Object.assign({op:'×'},pa));
  const rd=[
  {t:'第 15 回 二位數乘以一位數',secs:npSecs('15',[
    {k:'mx',t:'一、寫成直式算算看',d:'',P:48,items:[X({z:'t'}),X({z:'t'}),X({la:2}),X({la:2}),X({la:2}),X({la:2}),X({la:2,c:1}),X({la:2,c:1})]},
    {k:'wp',t:'二、先用算式記下來，再用直式算算看',d:'',P:52,items:[W('mul2'),W('mul2'),W('mul2'),W('mul2'),W('mul2'),W('mul2'),W('mul2')]}])},
  {t:'第 16 回 三位數乘以一位數',secs:npSecs('16',[
    {k:'mx',t:'一、寫成直式算算看',d:'',P:40,items:[X({z:'h'}),X({z:'h'}),X({la:3,c:0}),X({la:3,c:0}),X({la:3,c:1}),X({la:3,c:1}),X({la:3,c:1}),X({m0:1,la:3})]},
    {k:'mx',t:'二、下面哪一個學生的算法是對的？',d:'',P:12,items:[M('whoc')]},
    {k:'wp',t:'三、先用算式記下來，再用直式算算看',d:'',P:48,items:[W('mul3'),W('mul3'),W('mul3'),W('mul3'),W('mul3'),W('mul3')]}])},
  {t:'第 17 回 乘法估算',secs:npSecs('17',[
    {k:'mx',t:'一、幫忙估一估，選出答案',d:'',P:30,items:[M('est',{v:1}),M('est',{v:2}),M('est',{v:3}),M('est',{v:4})]},
    {k:'mx',t:'二、左邊的算式和右邊的哪一個算式答案最接近？',d:'',P:30,items:[M('estb'),M('estb'),M('estb'),M('estb'),M('estb')]},
    {k:'mx',t:'三、想想看，選出對的',d:'',P:24,items:[M('est',{v:6}),M('est',{v:7}),M('est',{v:8})]},
    {k:'mx',t:'四、估一估，把做法和答案記下來',d:'',P:16,items:[M('est',{v:9}),M('estf')]}])},
  {t:'第 18 回 第 4 單元複習(1)　基礎題',secs:npSecs('18',[
    {k:'mx',t:'一、寫成直式算算看',d:'',P:40,items:[X({z:'t'}),X({la:2}),X({la:2,c:1}),X({z:'h'}),X({la:3,c:0}),X({m0:1,la:3}),X({la:3,c:1}),X({la:3,c:1})]},
    {k:'mx',t:'二、把答案最接近的算式連起來',d:'',P:16,items:[M('lkq')]},
    {k:'mx',t:'三、看價目表，想一想',d:'',P:16,items:[M('menu')]},
    {k:'wp',t:'四、先用算式記下來，再用直式算算看',d:'',P:28,items:[W('mul2'),W('mul3'),W('mul3'),W('mul3')]}])},
  {t:'第 19 回 第 4 單元複習(2)　進階題',secs:npSecs('19',[
    {k:'mx',t:'一、填入＜、＝或＞',d:'',P:16,items:[M('cmpm'),M('cmpm'),M('cmpm'),M('cmpm')]},
    {k:'mx',t:'二、下面敘述對的選「對」',d:'',P:12,items:[M('stmt')]},
    {k:'mx',t:'三、自然科學博物館戶外教育活動',d:'',P:8,items:[M('bus')]},
    {k:'wp',t:'三、寫出做法和答案',d:'',P:16,items:[W('mul2'),W('mul2')]},
    {k:'wp',t:'四、先用算式記下來，再用直式算算看',d:'',P:48,items:[W('mul2'),W('mul2'),W('mul3'),W('mul3'),W('mul3'),W('mul3')]}])}
  ];
  return rd.filter(z=>z.secs.length);
}
/*PRIV:M4:END*/
