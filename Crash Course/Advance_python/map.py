def square(num):
    return num*num

# method1
l1=[2,3,4]
l2=[]
for i in l1:
    l2.append(square(i))
print(l2)

print(list(map(square,l1)))