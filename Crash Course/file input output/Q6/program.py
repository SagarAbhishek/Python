# with open('Crash Course\\file input output\\Q6\\log.txt') as f:
#     content=f.read()
# if 'Python' in content:
#     print('yes present')
content=True
i=1
with open('Crash Course\\file input output\\Q6\\log.txt') as f:
    while content:
        content=f.readline()
        if 'Python' in content:
            print(content) 
            print(f'yes present on line no {i}')
        i+=1

