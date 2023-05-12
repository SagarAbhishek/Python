myDisk={"fast":"in a quick manner",
        "Abhishek" : "a Data scientist",
        "marks":[1,2,3],
        "anotherdisk": {"sagar":"fitness freak"},
        1:2
    }
# myDisk["marks"]=[22,33,44]
# print(myDisk["marks"])
# print(myDisk["Abhishek"])
# print(myDisk['anotherdisk']['sagar'])

# Dictionary methods
# print(list(myDisk.keys())) prints the keys of the dictionary
# print(myDisk.values()) print the value of dictionary
# print(myDisk.items()) print the (key , value) of all the contant of the dictionary
# print(myDisk)
newDick={
    'diksha':'friend',
    'mukesh':'friend',
    'chandan':'bestfriend',
    'Abhishek':'a fitness'
}
# myDisk.update(newDick) #updates the dictionary by adding key value pairs from updatesdisk
# print(myDisk)

# print(myDisk.get('Abhishek')) #print value associated with key abhishek
# print(myDisk['Abhishek'])  #print value associated with key abhishek

#differenec between .get and [] syntex in dictionary
print(myDisk.get('abhishek'))# return None as abhishek is not present in dick
print(myDisk['abhishek']) # return an error as abhishek is not present in dick