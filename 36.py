def is_bin_palindromes(x):
	bstr = bin(x)[2:]
	return bstr[::-1] == bstr
def is_int_palindromes(x):
	s = str(x)
	return s[::-1] == s

print sum([i for i in xrange(1000000) if is_int_palindromes(i) and is_bin_palindromes(i)])
