import os
import numpy as np

dir = os.getcwd()

os.chdir('/usr/local/Homebrew/Library/Taps/homebrew/homebrew-cask/Casks')

casks = []

for i in os.listdir():
  for j in os.listdir(i):
    casks.append(j.split('.')[0])

os.chdir(dir)

with open('casklist.npy', 'wb') as f:
    np.save(f, casks)
