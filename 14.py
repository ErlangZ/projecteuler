large = 20
t = [0]*large

def chain_num(m):
	if t[m] != 0:
		return t[m]
	if m % 2 == 0:
		t[m] = chain_num(m/2)+1
	else:
		t[m] = chain_num(3*m+1)+1
	return t[m]

for i in xrange(large/4):
	chain_num(i)
print max(t[0:large/4])