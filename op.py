b="""

"""

b=b.split("\n")

for i in b:
  if i!='':
    l=i.split(": ")
    if l[0]!='':
      if l[1] not in ['unversioned','latest','discontinued','deprecated','versioned','disabled']:
        if l[0] not in ['Error','Warning','git','fatal']:
          m=l[1].split(' ==> ')[0]
          n=l[1].split(' ==> ')[1]
          if m!=n:
            print(i)
