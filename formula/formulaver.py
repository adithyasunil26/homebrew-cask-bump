import os
import re 

from formulaslist1 import a

b=a

b=b.replace("\n","\t").replace(" ","\t").split("\t")
c=[]
for k in b:
    if k!='':
        c.append(k)

for i in c:
    k=os.system("brew livecheck {}".format(i))