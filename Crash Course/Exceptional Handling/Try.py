while(True):
    print("Enter q for exit")
    n=input("Enter the number: ")
    if n=='q':
        break
    try:
        a=int(n)
        if a>6:
            print("number is greater than 6.")
    except Exception as e:
        print(f"Your input resulted in an error:{e}.")  

print("Thanks for playing.")  
    
    
    

