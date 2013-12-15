from operator import mul
times = 1000000 % reduce(mul, xrange(1, 11))

def next_permutation(word):
	rword = word[::-1]
	need_revert = True
	for loc in xrange(1, len(rword)):
		if rword[loc] < rword[loc-1]:
			need_revert = False
			break
	if True == need_revert:
		return rword
	for m in xrange(loc):
		if rword[m] > rword[loc]:
			break
	rword = "".join(["".join((rword[:m],rword[loc],rword[m+1:loc]))[::-1], rword[m],rword[loc+1:]])
	return word[:len(word)-loc-1] + rword[:loc+1][::-1]

p = "0123456789"
for i in xrange(times-1):
	p = next_permutation(p)

print p

