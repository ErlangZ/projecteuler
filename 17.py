table = {
	0:"zero",
	1:"one",
	2:"two",
	3:"three",
	4:"four",
	5:"five",
	6:"six",
	7:"seven",
	8:"eight",
	9:"nine",
	10:"ten",
	11:"eleven",
	12:"twelve",
	13:"thirteen",
	14:"fourteen",
	15:"fifteen",
	16:"sixteen",
	17:"seventeen",
	18:"eighteen",
	19:"nineteen",
	
	20:"twenty",
	30:"thirty",
	40:"forty",
	50:"fifty",
	60:"sixty",
	70:"seventy",
	80:"eighty",
	90:"ninety",
	100:"hundred",
}

def translate(n):
    if n <= 20:
        return table[n]
    elif n < 100:
        if n % 10 != 0:
            return table[n/10*10]+" "+table[n%10]
        else:
            return table[n/10*10]
    elif n < 1000:
        if n % 100 == 0:
            return table[n/100]+" hundred"
        else:
            return table[n/100]+" hundred and "+translate(n%100)
    else:
        return "one thousand"
    
print 1, translate(1)
print 21,translate(21)
print 20, translate(20)
print 30, translate(30)
print 99,translate(99)
print 100,translate(100)
print 110,translate(110)
print 120,translate(120)
print 101,translate(101)
print 121,translate(121)
print 130,translate(130)
print 131,translate(131)
print 199,translate(199)
print 999,translate(999)
print 1000,translate(1000)

print sum([len(translate(i).replace(" ", ""))for i in xrange(1,1001)])
