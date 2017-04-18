# Print the opening of "The World Was Wide Enough"
count = 1

while count < 10:
	print count
	count += 1
else:
	print "There are 10 things you need to know"
	count = 0
# Break clauses just end the loop. Use case?

# Continue
print "Playing with continue"

while count < 10:
	print "The count is currently", count, "Adding 1 to the count"
	count += 1

	if count == 8:
		print "Did you know I was born on the 8th?"
	else:
		"Continuing ..."
	continue

# Pass
