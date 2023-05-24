try:
    a=int(input("ENTER THE NUMBER:"))
except Exception as e:
    print(e)
    exit()

finally:
    print("We were Successful.")

print("Thanksssssss.")