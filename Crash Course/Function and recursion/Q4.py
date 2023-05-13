def sum_natural(num):
    if(num==1):
        return 1
    else:
       return(num+sum_natural(num-1))
    
n=int(input('enter the number: '))
print(sum_natural(n))
