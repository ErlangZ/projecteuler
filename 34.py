# coding:utf8
#from __future__ import print_function
import operator
# Waring：0的阶乘是1
X = [1]+[reduce(operator.mul, xrange(1, i+1)) for i in xrange(1,10)]

#method1
#任何一个8位数，它的数字阶乘和最多只有7位 9!*8，那么这是搜索的上限
# ca, 11s就跑完了
def digit_factorials_sum(x):
	return sum([X[int(i)] for i in str(x)])
large = 8*X[9]
print [i for i in xrange(1, large) if digit_factorials_sum(i) == i]


# method2
# A -> Ax       ==> A*10+x = A      + 9*A+x
# F(A)->F(Ax)   ==>          F(A)   + x!
# 初始情况下， a=[0,9] 毫无疑问，F(a) >= a，而F是线性增长的
# 而A的增长是指数的，一旦Ａ>F(A)，它会越来越快。F再也追不上他，我们可以利用这点
# 这个方法比较慢,跑了差不多15分钟
result = []
def search(A, F):
	if A == F: 
		result.append(A)
	if A > F and A*10+9 > F+X[9] :
		return False
	return [(A*10+i, F+X[i]) for i in range(10)]

R = [(i,X[i]) for i in xrange(1,10)]
while len(R) != 0:
	r = search(*R[0])
	if r != False:
		R.extend(r)	
	del R[0]
print (result)