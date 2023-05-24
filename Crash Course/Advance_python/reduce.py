from functools import reduce

sum= lambda a,b:a+b
l1=[1,2,3,4]
print(reduce(sum,l1))