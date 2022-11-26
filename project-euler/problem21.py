import time
from math_lib import generate_primes_range

start_time = time.time()

def get_divisors_sum(n):
    sum_d  = 0
    for d in range(1,int(n/2 + 1)):
        if n%d == 0:
            sum_d += d
    return sum_d

n = 1
embicle_sum = 0
while n < 10000:
    dofa  = get_divisors_sum(n)
    if (n == get_divisors_sum(dofa)) & (dofa < 10000) & (n != dofa):
        embicle_sum += dofa
        print(f'embicle:{n}-{dofa} sum {embicle_sum}')
    n += 1
    #quit()
print(embicle_sum)

print(f'Execution duration : {time.time() - start_time}')