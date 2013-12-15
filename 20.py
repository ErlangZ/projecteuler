import operator
print sum([int(x) for x in list(str(reduce(operator.mul, xrange(1, 101))))])
