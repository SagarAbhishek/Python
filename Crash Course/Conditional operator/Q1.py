num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2st number: "))
num3=int(input("enter the 3st number: "))
num4=int(input("enter the 4st number: "))
if(num1>num2 and num1>num3 and num1>num4):
    print(str(num1)+' is greater')
if(num2>num1 and num2>num3 and num2>num4):
    print(str(num2)+' is greater')
if(num3>num2 and num3>num1 and num3>num4):
    print(str(num3)+' is greater')
if(num4>num2 and num4>num3 and num4>num1):
    print(str(num4)+' is greater')