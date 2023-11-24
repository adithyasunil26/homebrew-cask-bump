import os
import numpy as np
from tqdm import tqdm
from datetime import date


with open('casklist.npy', 'rb') as f:
    a = np.load(f)

with open('casklist_old.npy', 'wb') as f:
    np.save(f, a)

print("Number of casks = "+str(np.size(a)))


# Put names of casks to remove manually in this array
manual_removal_casks=[]

print("Removing manually selected casks")
for i in manual_removal_casks:
    a=np.delete(a,np.where(a==i))
print("Number of casks = "+str(np.size(a)))

logfilename=str(date.today())

with open(logfilename, 'r') as file:
    op = file.read().split('\n')

auto_removal_casks=[]

for i in tqdm(op):
    if i!='':
        l=i.split(": ")
        if l[0]!='':
            if l[1] in ['unversioned','latest','discontinued','deprecated','versioned','disabled'] or l[0] in ['Error','Warning','git','fatal'] or l[1].startswith('skipped - '):
                auto_removal_casks.append(l[0])

print("Removing automatically filtered casks")
for i in tqdm(auto_removal_casks):
    a=np.delete(a,np.where(a==i))
print("Number of casks = "+str(np.size(a)))

with open('casklist.npy', 'wb') as f:
    np.save(f, a)
