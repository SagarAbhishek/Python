def remove_and_strip(string, word):
    newStr=string.replace(word," ")
    return newStr.strip()

post='     sagar is a good boy   '
n=remove_and_strip(post,'sagar')
print(n)
# print(post.strip()) #remove space