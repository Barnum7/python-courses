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
