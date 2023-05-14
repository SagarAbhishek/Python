def game():
    return 500
score=game()
with open('Crash Course\\file input output\\HIghscore.py')as f:
    HighScore=f.read()
if(HighScore==''):
    with open('Crash Course\\file input output\HIghscore.py','w')as f:
        f.write(str(score))
elif(int(HighScore)<score):
    with open('Crash Course\\file input output\HIghscore.py','w')as f:
        f.write(str(score))
    

