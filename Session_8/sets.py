tags = {"ai", "python", "data-structures"}

print(tags)

# adding some value
tags.add("machine-learning")
tags.remove("python")

for i in tags:
    print(i)


 # Union
a = {1, 2, 3}
b = {3, 4, 5}

# union of a and b

c = a | b
print(c)

# common elements in a and b
d = a & b
print(d)

# difference of a and b

e = a - b
print(e)

