import re,sys
s=open(sys.argv[1],encoding='utf8').read()
s2=re.sub(r'/\*PRIV:(M\d+):BEGIN.*?/\*PRIV:\1:END\*/\n?','',s,flags=re.S)
open(sys.argv[2],'w',encoding='utf8').write(s2)
print(len(s),'->',len(s2))
