def greeting(name):
	print "Greetings", name

greeting("Brian")


# A Function with a return value. Super useless and contrived function. Just covering syntax
def get_name(name):
	return name

my_name = get_name("Brian")
print my_name

# A function to see if a number is prime
def is_prime(num):
	"""
	This function checks for prime number.
	This is different than the udemy course. I had to include multiple breaks to fully escape the functionnn
	"""
	for n in range(2,num):
		if num % n == 0:
			print 'Not Prime'
			break
		else:
			print "You've found a prime!"
		break

is_prime(13)
is_prime(12)
