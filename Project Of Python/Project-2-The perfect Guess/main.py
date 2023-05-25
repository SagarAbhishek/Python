import random
randNo=random.randint(1,100)
print('Game started')
userGuess=None
guesses=1
while(userGuess!=randNo):
    guesses+=1
    userGuess=int(input('Guess a number:  '))
    if(userGuess>randNo):
        print('Lower number please: ')
    elif(userGuess<randNo):
        print('Higger number please: ')        
    elif(userGuess==randNo):
        print(f'Cogratulation ! You guessed the number in {guesses} Attempt.')
        break
    
with open('Crash Course\\Project-2-The perfect Guess\\highScore.txt') as f:
    highScore=int(f.read())
if(highScore>guesses):
    print('Cogratulation ! You break the highest record.')
    with open('Crash Course\Project-2-The perfect Guess\highScore.txt','w')as f:
        f.write(str(guesses))
    
    

    

