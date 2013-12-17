import math
def is_prime(m):
	if m < 0: return False
	return not any([m%f == 0 for f in xrange(2, int(math.sqrt(m))+1)])

m = 0
r = 0
for a in range(-1000,1000):
	for b in range(-1000, 1000):
		i = 0
		n = 0
		while True:
			if not is_prime(n**2+n*a+b):
				if i > m:
					m = i
					r = a*b
				break
			i += 1
			n += 1
print r