n=int(input("Enter the number: "))

table=[n*i for i in range(1,11)]
with open("Crash Course\\Exceptional Handling\\pratices_Set\\table.txt",'a')as f:
    f.write(str(table))
    f.write('\n')
