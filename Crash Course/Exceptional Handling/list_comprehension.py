a=[3,6,5,6,9,8,16,1,6,36,8]
b=[]
for item in a:
    if item%2==0:
        b.append(item)
print(b)


# shortcut
c=[i for i in a if i%2==0]
print(c)

t=[1,4,2,4,1,2,3]
s={i for i in t}
print(s)    