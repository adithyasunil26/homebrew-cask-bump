import os
import re 
import sys
from datetime import date

from casklist import a

logfilename=str(date.today())

a=a.replace("\n","\t").replace(" ","\t").split("\t")
for k in a:
    if k!='':
      os.system("brew livecheck {} >> {}".format(k,logfilename))

with open(logfilename, 'r') as file:
  op = file.read().split('\n')

for i in op:
  if i!='':
    l=i.split(": ")
    if l[0]!='':
      if l[1] not in ['unversioned','latest','discontinued','deprecated','versioned','disabled','skipped - unversioned URL','skipped - No version information available','skipped - only works with POST request','skipped - unversioned QT application','skipped - unversioned Java application','skipped - No reliable way to get version info','skipped - version is contained in the mounted DMG volume name']:
        if l[0] not in ['Error','Warning','git','fatal']:
          name=l[0]
          m=l[1].split(' ==> ')[0]
          n=l[1].split(' ==> ')[1]
          if m!=n:
            # print(i)
            command="brew bump-cask-pr --version={} {}".format(n,name)
            print(command)
            #os.system(command)