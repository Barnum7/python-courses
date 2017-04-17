# A dictionary is a hash table
my_name = {
	'first_name' : 'Brian',
	'middle_name' : 'James',
	'last_name' : 'Groat'
}

print my_name
print my_name['middle_name'] #What is my middle name?

# What is the first letter of my last name?
print my_name['last_name'][0]

# Change your middle name to an initial and print your name
my_name['middle_name'] = my_name['middle_name'][0]
print "%s %s %s" %(my_name['first_name'], my_name['middle_name'], my_name['last_name'])

# Adding keys by assignment
my_dog = {}
print my_dog

my_dog['name'] = 'Franklin'
print my_dog

my_dog['owner'] = my_name
print my_dog['owner']

print my_dog['owner']['first_name'].upper()

print my_name.keys()
print my_name.values()

print my_dog.keys()
print my_dog.values()