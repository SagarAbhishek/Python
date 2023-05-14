# f=open('Crash Course\\file input output\\sample.txt','r')
# data=f.read(10)
# print(data)
# f.close()

# f=open('Crash Course\\file input output\\sample.txt','r')
# data=f.readline()
# print(data)
# data=f.readline()
# print(data)
# f.close()

# f=open('another.txt','w')
# f.write(' i am appendin g')
# f.close()

with open('Crash Course\\file input output\\sample.txt','r') as f:
    a=f.read()
    print(a)

with open('another.txt','w') as f:
    a=f.write('me')
    print(a)