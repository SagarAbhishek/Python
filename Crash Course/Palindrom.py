def palindrom(n):
    number=0
    while(n):
        r=n%10
        number=number*10+r
        n=n//10
    return number

if __name__=='__main__':
    n=int(input("Enter the number:"))
    reverse=palindrom(n)
    print('The given is Palindrome' if(n==reverse) else 'The given number is not Palindrome')