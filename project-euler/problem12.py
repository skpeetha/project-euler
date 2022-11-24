# tringluar numbers
import time
from math_lib import generate_primes_range

start_time = time.time()
i = 3
n = 6 #sum of first i digits

primes = [2]
startR = 3


def m_list(num,f_list):
    f_set = set()
    for f in f_list:
        f_set.add(num*f)
    return f_list[0]*num,f_set

#print(m_list(4,[2,3,3,5]))
#quit()

if n < startR:
    print(f'min start values should be 2')
    quit()

while True:
    endR = int(n/2 + 1)
    primes = primes + generate_primes_range(startR,endR)
    #2 3 5 7 11 13
    factors = [] #prime factors of n
    di = {1} # divisors of n
    for p in primes:
        res = n
        count = 0
        bflag = False
        while res%p == 0:
            res = int(res/p)
            di.add(p)
            di.add(res)
            factors.append(p)
            if res in primes:
                factors.append(res)
                bflag = True
                break
        if bflag:
            break

    #print(f'factors {n}: {factors}')
    for it,p in enumerate(factors):
        temp_lt =  factors[it:]
        prd = p
        while len(temp_lt) > 1:
            prd, temp_set = m_list(prd,temp_lt[1:])
            di = di.union(temp_set)
            temp_lt = temp_lt[1:]

    if len(di) > 500:
        print(f'Number : {factors}')
        print(f'iterator: {i} divisors of {n}: -- {len(di)}')
        print(f'Execution duration : {time.time() - start_time}')
        quit()
    print(f'iterator: {i} divisors of {n}: -- {len(di)}')
    startR = endR
    i = i + 1
    n = int(i*(i+1)/2)
    



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