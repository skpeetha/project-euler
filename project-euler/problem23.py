import time
from math_lib import generate_primes_range

start_time = time.time()

def get_divisors_sum(n):
    sum_d  = 0
    for d in range(1,int(n/2 + 1)):
        if n%d == 0:
            sum_d += d
    return sum_d

n = 12



while n < 28123


print(f'Execution duration : {time.time() - start_time}')