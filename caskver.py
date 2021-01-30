import os
import re 

#from caskslist1 import a
#from caskslist4 import d
from caskslist5 import e
#from caskslist6 import f
#from caskslist7 import g

#1 3 done 31/01/21

b=e

b=b.replace("\n","\t").replace(" ","\t").split("\t")
c=[]
for k in b:
    if k!='':
        c.append(k)

for i in c:
    k=os.system("brew livecheck {}".format(i))

