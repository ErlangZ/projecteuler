with open("./names.txt") as f:
	lines = f.readline().split(',')
	lines.sort()
	print sum([sum([ord(a)-ord('A')+1 for a in l.strip("\"")])*(i+1) for i, l in enumerate(lines)])
		