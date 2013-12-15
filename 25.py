f_n_1 = 1
f_n_2 = 1
i = 2
while True:
	f_n = f_n_1+f_n_2
	if len(str(f_n)) >= 1000:
		print i+1
		break
	f_n_1, f_n_2 = f_n, f_n_1
	i += 1
