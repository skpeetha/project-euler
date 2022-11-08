# tringluar numbers
i = 2
current_tn = 3
while True:
	count = 1
	for f in range(1,int(current_tn/2)+1):
		if current_tn%f == 0:
			count = count + 1
			
			if count > 500:
				print(f'iteration:{i}\ntriangular number:{current_tn}')
				quit()
	print(f'i:{i} tn:{current_tn} Divisors:{count}')
	i = i + 1
	#print(i)
	current_tn = i*(i+1)/2