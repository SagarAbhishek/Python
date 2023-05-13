# def greet(name='stranger'):
#     return('Have a good day '+name)
# name=input('Enter your name: ')
# # print(greet(name))
# print(greet())

# def recursion(num):
#     multi=1
#     for i in range(1,num+1):
#         multi*=i
#     return(multi)    

def fact(num):
    recursion=0
    if(num==1 or num==0):
        return 1
    else:
        return (num*fact(num-1))

num=int(input('Enter your number: '))
print(fact(num))
