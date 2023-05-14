import os
oldname='Crash Course\\file input output\\Q9\\sample3.txt'
newname='Crash Course\\file input output\\Q9\\renamedfile.txt'

with open(oldname)as f:
    content=f.read()
with open(newname,'w')as f:
    f.write(content)

os.remove(oldname)