import os
from casktorem import k
from caskslist7 import g

a=g
l=k

for i in l:
#  print(i)
  if i in a:
    a=a.replace(i,'')

print(a)