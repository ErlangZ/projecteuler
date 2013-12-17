large = 10000000000
print sum([(i**i)%large for i in xrange(1, 1001)])%large