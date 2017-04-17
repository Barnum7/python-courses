#A list is just like an array!
my_list = ['This', 'is', 'a', 'list']
print my_list

my_mixed_list = ['This', 22, 3.14, 'data'] #arrays can hold multiple data types
print my_mixed_list

print len(my_list)
print len(my_mixed_list) #You can get how many items are in a list

print my_list[1] #Get a list item by index
print my_mixed_list[1:] #get everything after index value 1\

my_mixed_list = my_mixed_list + ['adding an item to the list']
print "my_mixed_list is now {my_mixed_list}".format(my_mixed_list = my_mixed_list)

print my_mixed_list * 2

my_list.append("I appended this") #add an item to the end of the list

print my_list

print my_list.pop() #By default this takes off the last index. However you can pass it an index as an argument.
print my_list #The list has been permenantly changed by pop()

new_list = ['b', 'r', 'i', 'a', 'n']

new_list.reverse() #reverses the list
print new_list

new_list.sort() #sorts the list
print new_list

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1,l_2,l_3] #you can create nested lists

print matrix

print matrix[1][1] #How would you get the value 5 from this structure?
