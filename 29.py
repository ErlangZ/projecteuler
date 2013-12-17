large = 100

#method 1
print len(set([a**b for a in xrange(2, large+1) for b in xrange(2, large+1)]))


#method 2, 最开始的思路是将b化简划到a的某次幂上，注意(43,3)这个用例
table = [1]*(large+1)
table[0] = 0
table[1] = 0
for i in xrange(2, large+1):
	j = 2
	while i*j <= large:
		table[i*j] = 0
		j+=1
prime_table = [i for i, x in enumerate(table) if x != 0]

#prime resolve, return (p,x)
def prime_resolve(x, p):
        r = 0
        while x % p == 0:
                r += 1
                x /= p
        return p,r

def prime_resolve_num(x):
	return [r for p,r in [prime_resolve(x, p) for p in prime_table]]

def induct(a, b):
	return [r*b for r in prime_resolve_num(a)]

X = list()
R = 0
for a in xrange(2, large+1):
	for b in xrange(2, large+1):
		r = induct(a,b)
		if r not in X:
			X.append(r)
			R += 1
print R
