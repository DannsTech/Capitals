word = input("write a word with capitals and lowecarse: ")
list = []
list2 = []
for i in word:
    list.append(i)
for x in list:
    if x == x.upper():
        index = list.index(x)
        list2.append(index)

print(list)
print(list2)

##Done