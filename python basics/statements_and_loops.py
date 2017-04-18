names = ["Brian","Erika","Chris"]

for name in names:
	if name == "Brian":
		print "Hello Master"
	elif name == "Erika":
		print "Hello Lady"
	else:
		print "Da Fuck are you?"

pets = ["Dog", "Cat", "Platypus"]

for pet in pets:
	if pet == "Dog":
		print "What a cute puppy!"
	elif pet == "Cat":
		print "I'm really more of a dog person"
	else:
		print "Da Fuck is that?"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

for number in numbers:
	if number%2 == 0:
		print number, "is even"
	else:
		print number, "is odd"

animals = ["Dogs", "Cats", "Horses", "Cows", "Camels"]

for animal in animals:
	print "Noah got two", animal

# FizzBuzz Implementation
for number in numbers:
	if number%2 == 0 and number%3 == 0:
		print "FizzBuzz"
	elif number%2 == 0:
		print "Fizz"
	else:
		print number

list_sum = 0

for number in numbers:
	list_sum += number

print list_sum

# You can also iterate through a string
my_name = "Brian James Groat"

for letter in my_name:
	print letter



# Iterating nested tuples

# One level deep
list_of_tuples = [(1,2),(3,4),(5,6)]

for item in list_of_tuples:
	print item

# Two Levels Deep
for item in list_of_tuples:
	for objects in item:
		print objects

# You can also do tuple unpacking
print "Tuple Unpacking"
for (t1, t2) in list_of_tuples:
	print t1 + t2

# Iterating through a dictionary and printing the values
my_dict = {
	"first_name" : "Brian",
	"middle_name" : "James", 
	"last_name" : "Groat"
}
print "Printing Dictionary values"

for k,v in my_dict.iteritems():
	print "My", k , "is", v
