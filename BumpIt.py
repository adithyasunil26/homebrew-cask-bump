import os
import numpy as np
from tqdm import tqdm
from datetime import date

with open('casklist.npy', 'rb') as f:
    a = np.load(f)

logfilename=str(date.today())
scriptfilename=str(date.today())+'_script.sh'

for k in tqdm(a):
    if k!='':
      os.system("brew livecheck {} >> {}".format(k,logfilename))

with open(logfilename, 'r') as file:
  op = file.read().split('\n')

with open(scriptfilename, 'a') as file:
  for i in tqdm(op):
    if i!='':
      l=i.split(": ")
      if l[0]!='':
        if l[1] not in ['unversioned','latest','discontinued','deprecated','versioned','disabled','skipped - unversioned URL','skipped - No version information available','skipped - only works with POST request','skipped - unversioned QT application','skipped - unversioned Java application','skipped - No reliable way to get version info','skipped - version is contained in the mounted DMG volume name']:
          if l[0] not in ['Error','Warning','git','fatal']:
            name=l[0]
            m=l[1].split(' ==> ')[0]
            n=l[1].split(' ==> ')[1]
            if m!=n:
              command="brew bump-cask-pr --version={} {}".format(n,name)
              file.write(command+'\n')
              # print(command)
              #os.system(command)