# from __future__ import print_function

# In python strings have a property called immutability. This means that you cannot change the data once it is set. However you can concate data to it. Or reassign the entire variable
# You can use single or double quotes to create strinsg
print "Hello"
print 'world'

# \n makes a new line. Having a space after that will make a new line + spafce
print "Hello friend \nMy name is Asimov"

# \t makes a tab
print "Here comes a \t tab"

# print("This is how you print in Python 3")

print len("Hello friend") #The length of the string

x = "Hello friend"

print "Hello friend has how many characters? ", len(x)

print x[0] #The string starts at 0 index
print x[6] #item at 6th index (the 7th place)

print x[1:] #this grabs everything from the 1st index to the end
print x[1:5] #this prints everything from the 1st index to the 5th index
print x[:3] #this prints everything up to (but not including) the 3rd index

print x[:] #this means grab everything. What is the use case?

print x[-1] #this grabs the last letter
print x[-2] #the second last item
print x[:-1] #grab everything up to the last letter

print x[::1] #grabs everything (first colon) with intervals of 1 (the second colon and the number)
print x[::2] #grabs everything (with a 2 interval, so every other character)

print x[::-1] #prints the strong backward (starting at -1 index)

print x.upper() #This calls the upper case method on my string
print x.lower() #the lower case function on my string

print x.split('e') #This splits my string whereever an 'e' occurs

# Examples of String Interpolation
s = 'string'

print "How many letters are in 'string'? %s" %(len(s))

print "Floating point number: %1.2f" %(3.1415) #The digit to the left of the decimal tells you the minimal number of digits in the number. The number to the right tells you how many digits to float to. The f tells you that it is a floating point number

print "My name is %s. My brothers are %s, %s, %s, and %s" %('Brian', 'Cody', 'Derek', 'Scott', 'Ian') #Interpolate the strings in the order they are passed as arguments

print "{surname}. Brian {surname}".format(surname="Groat") #When you need to repeat the value you are interpolating.

print "{surname}. {first_name} {surname}".format(surname="Groat", first_name = "Brian") #You can also pass multiple arguments
