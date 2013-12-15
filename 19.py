days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def is_leap_year(y):
    if y % 100 != 0:
        return y % 4 == 0
    else:
        return y%400 == 0

def day_of_year(y):
    if is_leap_year(y):
        return 366
    else:
        return 365

r = 0
d = day_of_year(1900)%7+1

for y in xrange(1901, 2001):
    for m in xrange(1,13):
        if d % 7 == 0:
            r+=1
        d = d + days[m]
        if m == 2 and is_leap_year(y):
            d += 1
print r

