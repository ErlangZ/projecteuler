def find_cycle(x):
	table = [None]*x
	I = 9
	i = 0
	while True:
		loc = I % x
		if table[loc] == None:
			table[loc] = i
		else:
			return i - table[loc]
		i += 1
		I = I * 10 + 9

print max([(find_cycle(i), i) for i in xrange(1, 1000)])
