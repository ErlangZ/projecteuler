large = 28124

#get the prime table
num_table = [1]*large
for i in xrange(2, large+1):
	j = 2
	while i * j < large:
		num_table[i*j] = 0
		j+=1
prime_table = [i for i,x in enumerate(num_table) if x == 1 and i > 1]

#prime resolve, return (p,x)
def prime_resolve(x, p):
        r = 0
        while x % p == 0:
                r += 1
                x /= p
        return p,r

def prime_resolve_num(x):
	return [(p,r) for p,r in [prime_resolve(x, p) for p in prime_table] if r > 0]

def get_factors(x):
	if x <= 0: return []
	factor_pairs = prime_resolve_num(x)
	result = [1]
	factor_t = [[p**i for i in xrange(r+1)] for p, r in factor_pairs]
	for f in factor_t:
		result = sum([[n*r for r in result] for n in f], [])
	return result[:-1]

abundant_nums = [x for x in xrange(1, large) if sum(get_factors(x)) > x]
abundant_nums_len = len(abundant_nums)
abundant_nums_sum = set([abundant_nums[x]+abundant_nums[y] for x in xrange(abundant_nums_len) for y in xrange(x, abundant_nums_len) if abundant_nums[x]+abundant_nums[y]<large])
print sum([x for x in xrange(large) if x not in abundant_nums_sum])
