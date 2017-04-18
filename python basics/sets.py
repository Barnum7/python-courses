# A set is an unordered sequence of unique elements

my_set = set()

my_set.add(1)
my_set.add("Brian")

print my_set

print my_set.add(1) #This will not work. Nothing will be added
print my_set

my_list = [1,1,1,2,2,2,3,3,4]
print set(my_list) #I can determine what the unique elements in a list are by using the set function
