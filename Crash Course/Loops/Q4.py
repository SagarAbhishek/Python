num=int(input('Enter a number: '))
count=True
for i in range(2,int(num/2)):
    if(num%i==0):
        count=False
        break

if(count):
    print('Prime')
else:
    print('not prime')

    