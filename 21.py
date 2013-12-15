large = 10000
#get the prime table
num_table = [1]*large
for i in xrange(2, large+1):
	j = 2
	while i * j < large:
		num_table[i*j] = 0
		j+=1
prime_table = [i for i,x in enumerate(num_table) if x == 1 and i > 1]

#prime resolve, return (p,x)
def prime_resole(x, p):
        r = 0
        while x % p == 0:
                r += 1
                x /= p
        return p,r

#get the sum of factor
from operator import add
def get_sum_of_factor(factor_pairs):
        result = [1]
        factor_t = [[p**i for i in xrange(r+1)] for p, r in factor_pairs]
        for f in factor_t:
                result = reduce(add, [[n*r for r in result] for n in f])
        return result

# find sum of factors
def find_pair(x):
        if x == 0:
                return -1
        l = [prime_resole(x, p) for p in prime_table if x > 0]
        return sum(get_sum_of_factor(l)[:-1])


r = []
for a in xrange(1, large):
        b = find_pair(a)
        if a != b and find_pair(b) == a:
                r.append(a)
print r, sum(r)
                        

