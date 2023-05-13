sub1=int(input('enter subject 1 marks: '))
sub2=int(input('enter subject 2 marks: '))
sub3=int(input('enter subject 3 marks: '))
if(sub1<33 or sub2<33 or sub3<33):
    print('fail')
elif(((sub1+sub2+sub3)/3)>40):
    print('pass')
else:
    print(' total fail')
