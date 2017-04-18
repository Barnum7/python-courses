import datetime

start = datetime.datetime.now()

for num in xrange(1, 1000000000):
	print num

print "This operation took"
print datetime.datetime.now() - start