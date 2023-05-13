n1=int(input('enter 1 st number: '))
n2=int(input('enter 2 st number: '))
n3=int(input('enter 3 st number: '))

def gretestNumber(a,b,c):
    if(a>b and a>c):
        print(str(a)+' is gretest')
    elif(b>a and b>c):
        print(str(b)+'  is gretest')
    else:
        print(str(c)+'  is gretest')



gretestNumber(n1,n2,n3)
