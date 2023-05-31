print("--------WELCOME TO KIRANA STORE--------")
add=0
while(True):
    n=input("Enter the Number for sum or press Q for Exit: ")
    if(n=='q'or n=='Q'):
        print("Thanks for Using our calculator")
        break
    else:
        add=add+int(n)
        print(f'Order total so far: {add}')

print(f"The sum of total Price is {add}")
    


