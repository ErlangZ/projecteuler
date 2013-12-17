print [i**5 for i in xrange(10)]
print sum([x for x in xrange(2, 600000) if sum([int(i)**5 for i in str(x)])==x ])