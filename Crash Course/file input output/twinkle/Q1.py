with open('Crash Course\\file input output\\poems.txt','r')as f:
    a=f.read()
if 'twinkle'in a:
    print('True')
else:
    print('False')
