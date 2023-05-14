words=["donkey", 'mota']
with open('Crash Course\\file input output\\Q5\\sample1.txt')as f:
    content=f.read()

for word in words:
    p=content.replace(word,'$$#$$@')
    print(p)
    with open('Crash Course\\file input output\\Q5\\sample1.txt','w')as f:
        f.write(p)