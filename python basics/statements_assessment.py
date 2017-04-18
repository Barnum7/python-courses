st = "Print only the words that start with s in this sentennce"

words = st.split(" ")

print words

for word in words:
	if word[0] == "s":
		print word

for num in range(11):
	if num % 2 == 0:
		print num

print "Numbers from 1-50 divisible by 3"
divisible_by_three = [number for number in range(50) if number % 3 == 0]
for number in divisible_by_three:
	print number

# Come back to
for word in words:
	if len(word) % 2 == 0:
		print "Even!"
	else:
		print word

# Fixx Buzz. Multiples of 3 Fizz. 5 Buzz. Go to 100

for number in range(100):
	if number % 3 == 0 and number % 5 == 0:
		print "FizzBuzz"
	elif number % 5 == 0:
		print "Buzz"
	elif number % 3 == 0:
		print "Fizz"
	else:
		print number

# Get a list of the first letters in the string of words

first_letters = [word[0] for word in words]
print first_letters