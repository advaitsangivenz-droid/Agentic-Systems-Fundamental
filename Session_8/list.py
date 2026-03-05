score = [2, 4, 9, 5]
# index = 1, 2, 3, 4
# index always starts with 0

# name of the list index
value = score[1]
print(value)

# Modifying Lists

# adding some value
# removing some value
# replicating some value

marks = [ 55, 87, 96, 77, 79]
# index =  0   1   2   3   4
# add a new subject mark at the end
# marks = [ 55, 87, 96, 77, 79, 90]

marks.append(90)
print(marks[5])

# To add something at the end of something use append function

# remove mark 55

print(marks[1])
marks.remove(55)
print(marks[1])

# update a value

attendence = [ 80, 90, 95, 85, 88]
# index =       1   2   3   4   5
# update attendence of 4th student to 90
attendence[3] = 90
print(attendence[3])



# List Slicing

marks = [ 55, 87, 96, 77, 79]

# want a smaller list
# world_list_1 = [ 55, 87, 96]
# world_list_2 = [ 77, 79, 90]
# world_list_3 = [ 55, 87, 96, 77, 79]

# list slicing 

world_list_1 = marks[0:3]
# give me the list starting from index 0 to index 3 but not including index 3
print(world_list_1)

world_list_2 = marks[3:6]
print(world_list_2)

world_list_3 = marks[0:6]
print(world_list_3)


# insert using index
marks = [ 55, 87, 96, 77, 79]
marks.insert(2, 100) # insert index and a value
print(marks[2])

marks = [ 55, 87, 96, 77, 79]
marks.pop(2) # remove the value at index 2
print(marks[2])