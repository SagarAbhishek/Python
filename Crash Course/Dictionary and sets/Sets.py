s={1,2,4,5,1} #collection of non repetative element
print(type(s))
print(s)

a={} #create an empty dictionary
print(type(a))
b=set() # create an empty set
print(type(b))
b.add(3)
b.add(4)
b.add(2)
b.add(2) # adding repleted value does not change the sets
b.add((7,8))# cannot add list and dictionary to sets
print(b)

# sets method

# print(len(b)) print the length of sets
# b.remove(2)

# print(b.pop()) remove arbitery element from the sets
# b.clear() empty the set
print(b)