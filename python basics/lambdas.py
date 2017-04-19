def square(num):
	result = num**2
	return result

print square(4)

# Simplfy
def square(num):
	return num**2

print square(3)

# To Named Lambda
square = lambda num: num**2
print square(2)

# Is a number even?
even = lambda num: num % 2 == 0

print even(4)
print even(5)
print even(6)

# To FunctionS

def even(num):
	return num % 2 == 0

print even(7)
print even(8)
print even(9) 