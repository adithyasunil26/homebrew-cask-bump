import os
from casks import a 

b=a.split('\n')

for i in b:
  cmd='brew install --cask {}'.format(i)
  print(cmd)
  os.system(cmd)
  os.system('open -a {}'.format(i))
  os.system('brew cask createzap {}'.format(i)+'> ./output.txt')

#doesnt work