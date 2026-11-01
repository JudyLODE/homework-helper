F='/mnt/user-data/outputs/study-helper.html'
s=open('/home/claude/study-helper.v59.html',encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a))
    s=s.replace(a,b)
ex=open('ex1.js',encoding='utf8').read()
rep("\nloadDict();\n","\n"+ex+"\nloadDict();\n")
# render map
rep("paper:paperV,full:fullV,settings:settingsV}[S.v]()","paper:paperV,full:fullV,settings:settingsV,exam,examprint}[S.v]()")
# click routing
rep("  if(a.startsWith('p_')||a==='paperhome'){ppClick(b);return}","  if(a.startsWith('p_')||a==='paperhome'){ppClick(b);return}\n  if(a.startsWith('ex_')){exClick(b);return}")
rep("  else if(a==='settings'){S.v='settings'}","  else if(a==='settings'){S.v='settings'}\n  else if(a==='exam'){S.v='exam';S.exMsg='';S.exd=-1}")
# home button + exclude exam from star totals
rep("  ${diary()}\n  <button class=\"go alt\" style=\"margin-top:18px\" data-a=\"settings\">","  ${diary()}\n  <button class=\"go\" style=\"margin-top:18px\" data-a=\"exam\">🧾 考卷出題</button>\n  <button class=\"go alt\" style=\"margin-top:10px\" data-a=\"settings\">")
rep("if(!s.del)s.m.forEach(m=>{if(SM.includes(m)){max+=3;tot+=star(i,m)}})","if(!s.del&&!(s.pp&&s.pp.ex))s.m.forEach(m=>{if(SM.includes(m)){max+=3;tot+=star(i,m)}})")
# MREGEN: exam = no 闖關
rep("const MREGEN=(k,sec)=>!!(MATH[k]&&MATH[k].gen&&(!sec||!MATH[k].can||sec.items.every(MATH[k].can)));","const MREGEN=(k,sec)=>!!(MATH[k]&&MATH[k].gen&&(!sec||!MATH[k].can||sec.items.every(MATH[k].can)));\nconst MREGN=(k,sec)=>MREGEN(k,sec)&&!(S.s>=0&&SEC[S.s]&&SEC[S.s].pp&&SEC[S.s].pp.ex);")
rep("  if(!sec||!MREGEN(sec.k,sec))return false;\n  const rd=","  if(!sec||!MREGN(sec.k,sec))return false;\n  const rd=")
rep("  if(!MREGEN(sec.k,sec))return ck?`<p class=\"secsc\">${sc.got===sc.max?","  if(!MREGN(sec.k,sec))return ck?`<p class=\"secsc\">${sc.got===sc.max?")
rep("gate:MREGEN(sec.k,sec)?","gate:MREGN(sec.k,sec)?")
s=s.replace('版本 v59（11/1）','版本 v60（11/1）')
css="""
.sheet{background:#fff;color:#000;border-radius:6px;padding:14px 16px;max-width:794px;margin:10px auto;line-height:1.8}.sheet *{color:#000}.sheet .pq{background:#fff;border:0;border-bottom:1px dotted #999;border-radius:0;box-shadow:none;padding:6px 0;margin:0 0 6px}.sheet .pi{background:#fff;border:0;border-bottom:1.5px solid #000;border-radius:0}.sheet .tk2{background:#fff;border:0;box-shadow:none;padding:0 .25em;font:inherit}.sheet .tk2.cir{border:2px solid #000;border-radius:50%}.sheet .ans{background:#eee;border:1px solid #888;color:#000}.sheet .ctx,.sheet .bankbox{background:#fff;border:1px solid #000}.sheet .exh h1{font-size:1.4rem;text-align:center;margin:0 0 6px}.sheet .exf{text-align:center;margin:4px 0}.sheet .exr{text-align:center;font-size:.85rem;margin-bottom:8px}.sheet .exs h3{font-size:1.1rem;margin:14px 0 4px;border-bottom:2px solid #000}.sheet .exp{font-weight:400}.sheet .exd{margin:0 0 4px}.sheet .ansmode .mk{display:none}.sheet svg{filter:grayscale(1)}.sheet .bk,.sheet .bill,.sheet .coin{filter:grayscale(1)}
@media print{@page{size:A4;margin:12mm}html,body{background:#fff!important}.noprint,#spd,.spdb{display:none!important}#app{padding:0!important;margin:0!important;max-width:none!important}.sheet{padding:0;margin:0;max-width:none;font-size:11pt;border-radius:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}.sheet .pq{break-inside:avoid}.sheet .exs h3{break-after:avoid}}
"""
k=s.index('.rl{width:100%;max-width:360px'); j=s.rfind('\n',0,k)+1
s=s[:j]+css+s[j:]
open(F,'w',encoding='utf8').write(s)
print('ok')
