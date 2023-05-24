def increment(n):
    try:
        return int(n)+1
    except:
        raise ValueError("This is not good Sagar")
 
print(increment('sd52'))