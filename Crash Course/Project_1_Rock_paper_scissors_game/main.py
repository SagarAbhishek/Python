import random

def gameWin(comp,you):
    if comp==you:
        print("tie")
    elif comp=='s':
        if you=='w':
            print('computer win')
        elif you=='g':
            print('you win')
    elif comp=='g':
        if you=='s':
            print('computer win')
        elif you=='w':
            print('you win')
    elif comp=='w':
        if you=='g':
            print('computer win')
        elif you=='s':
            print('you win')
    
        



print('computer choose: snake(s), water(w) and gun(g): ')
randNo=random.randint(1,3)
if(randNo==1):
    comp='s'
elif(randNo==2):
    comp='w'
else:
    comp='g'
you=input('chose snake(s), water(w) and gun(g): ')
print(f"computer choose: {comp} ")
print(f"You choose: {you} ") 
gameWin(comp,you)
