import os
import re 

#from caskslist1 import a
from caskslist6 import f

#1 3 done 31/01/21

b=f

b=b.replace("\n","\t").replace(" ","\t").split("\t")
c=[]
for k in b:
    if k!='':
        c.append(k)

for i in c:
    k=os.system("brew livecheck {}".format(i))
