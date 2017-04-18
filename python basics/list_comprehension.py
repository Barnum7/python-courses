letters_in_name = []

for letter in "Brian":
	letters_in_name.append(letter)

print letters_in_name

# With list comprehension

l = [letter for letter in "Brian"]

print l

evens = [number for number in range(11) if number % 2 == 0]

print evens

celsius = [0,10,20.1,34.5]

fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]

print celsius
print fahrenheit

# Nested list comprehension

nested = [x**2 for x in [x**2 for x in range(11)]]
print nested