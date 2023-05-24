def greater_than_5(num):
    if(num>5):
        return True
    else:
        return False
    
g5=lambda num:num>5
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(greater_than_5,l)))
print(list(filter(g5,l)))