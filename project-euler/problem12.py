# tringluar numbers
import time
from math_lib import generate_primes_range

start_time = time.time()
i = 3
n = 6 #sum of first i digits

primes = [2]
startR = 3

if n < startR:
    print(f'min start values should be 2')
    quit()

while True:
    endR = int(n/2 + 1)
    primes = primes + generate_primes_range(startR,endR)
    #2 3 5 7 11 13
    factors = {1,n}
    for p in primes:
        res = n
        count = 0
        bflag = False
        while res%p == 0:
            res = int(res/p)
            count = count + 1
            factors.add(p**count)
            factors.add(res)
            if res in primes:
                bflag = True
                break
        if bflag:
            break
    if len(factors) > 500:
        print(f'Number : {n}')
        print(f'Execution duration : {start_time - time.time()}')
        quit()
    print(f'iterator: {i} divisors of {n}: {factors} -- {len(factors)}')
    startR = endR
    i = i + 1
    n = int(i*(i+1)/2)
    

# iterator: 406 divisors of 82621: {1, 2849, 37, 7, 11, 29, 7511, 2233, 11803, 82621} -- 10
# actual 16 :1, 7, 11, 29, 37, 77, 203, 259, 319, 407, 1073, 2233, 2849, 7511, 11803, 82621



quit()
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