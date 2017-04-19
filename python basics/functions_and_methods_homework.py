import string #Importing the alphabet so I dooooooooooo't have to type it out

# Write a funtion that computes the volume of a sphere given its radius
def vol(radius):
	# Could be better, but I'm not using the math module to get an exact value for pi
	return  (4 * 3.14 * radius**3)/3

print vol(5)

# Write a function that checks whether a number is in a given range (inclusive of high or low)
def in_range(num,low,high):
	if num in range(low, high + 1):
		return True
	else:
		return False

print "Is 5 between 0 and 10?" , in_range(5,0,10)
print "Is 5 between 0 and 4?" , in_range(5,0,4)
print "Is 0 between 0 and 10?" , in_range(0,0,10)
print "Is 10 between 0 and 10?" , in_range(10,0,10)

# Wrie a function that calculates the number of upper and lowercase letters in a string
def upper_and_lower(string):
	words = string.split(" ")
	count = {
	"upper_case" : 0,
	"lower_case" : 0
	}

	for word in words:
		for letter in word:
			if letter.isupper():
				count["upper_case"] += 1
			else:
				count["lower_case"] += 1

	print string + " has", count["upper_case"], "upper case letters and", count["lower_case"], "lowercase letters"

upper_and_lower("Brian James Groat")
# Write a function that takes a list and returns a new list with unique items from that list
def unique_list(l):
	return set(l)

my_list = [1,1,2,3,5,8,2,4,5,3]

print unique_list(my_list)
# Write a function that multiplies all the numbers in a list
def multiply_num_in_list(l):
	total = 1
	for n in l:
		total *= n

	print total

multiply_num_in_list(unique_list(my_list))

# Write a function to tell if a string is a palindrome or not
def is_palindrome(s):
	s = s.lower()
	if s == s[::-1]:
		return True
	else:
		return False

print is_palindrome("Brian")
print is_palindrome("Racecar") 
# Write a function to tell if a string is a pangram (includes every letter in the alphabet at least once)
def is_pangram(s):
	s = s.lower()
	words_in_string = s.split(" ")
	letters_in_string = []

	for word in words_in_string:
		for letter in word:
			letters_in_string.append(letter)

	if sorted(set(letters_in_string)) == sorted(set(string.ascii_lowercase)):
		return True
	else:
		return False

print is_pangram("Brian")
print is_pangram("Waltz bad nymph for quick jigs vex")
print is_pangram("Quick zephyrs blow vexing daft Jim")
print is_pangram("Erika")