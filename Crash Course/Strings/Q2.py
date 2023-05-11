name=input("enter your name\n ")
date=input("enter today date\n")
letter='''Dear <|name|>
        You are selected
        <|date|>'''
letter=letter.replace('<|name|>',name)
letter=letter.replace('<|date|>',date)
print(letter)