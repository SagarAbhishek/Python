from functools import reduce
l1=[1,4,5,77,89,0,5,105]

# maximum=lambda a,b:max(a,b)
# print(reduce(maximum,l1))
print(reduce(max,l1))