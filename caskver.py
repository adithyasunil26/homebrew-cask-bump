import os
import re 
#from caskslist1 import a
#from caskslist2 import b
#from caskslist3 import c
from caskslist4 import d
#from caskslist5 import e
#from caskslist6 import f
#from caskslist7 import g

#1 2 3 done 24/01/21

b=d

b=b.replace("\n","\t").replace(" ","\t").split("\t")
c=[]
for k in b:
    if k!='':
        c.append(k)

for i in c:
    k=os.system("brew livecheck {}".format(i))

