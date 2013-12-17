nums = []
with open("triangle.txt") as ifile:
	for line in ifile:
		nums.append([int(num)for num in line.split()])

l = len(nums)

for i in xrange(1, l):
	for j in xrange(i):
		if j == 0:
			nums[i][j] += nums[i-1][j]
		elif j == l-1:
			nums[i][j] += nums[i-1][j-1]
		else:
			nums[i][j] += max((nums[i-1][j], nums[i-1][j-1]))

print max(nums[l-1])