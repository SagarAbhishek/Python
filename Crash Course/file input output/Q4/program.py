with open('Crash Course\\file input output\\Q4\\sample.txt')as f:
    content=f.read()
p=content.replace('donkey','fox')
with open('Crash Course\\file input output\\Q4\\sample.txt','w')as f:
    f.write(p)
