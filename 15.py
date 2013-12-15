import operator
r = reduce(operator.mul, range(1, 41))/(reduce(operator.mul, range(1,21)))**2
print r