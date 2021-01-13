import os

a="""


"""

a=a.split("\n")
for i in a:
    if i!='':
        l=i.split(":")
        name=l[0]
        m=l[1].split('==> ')[1]
        print(name,m)
        command="brew bump-formula-pr --version={} {}".format(m,name)
        print(command)
        os.system(command)