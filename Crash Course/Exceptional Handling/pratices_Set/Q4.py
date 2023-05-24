a=int(input("Enter the numbe is a: "))
b=int(input("Enter the number is b: "))

try:
    print(a/b)
except ZeroDivisionError as e:
    print("Infinite")

