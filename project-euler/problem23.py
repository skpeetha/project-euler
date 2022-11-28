#very inefficient method, took 1987 sec to complete
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
abd_n = []
nu = list(range(1,28123))

while n < 28123:
    if get_divisors_sum(n) > n:
        abd_n += [n]
        print(n)
    n += 1
len_abd = len(abd_n)
for ind,abd in enumerate(abd_n):
    #nu.remove(2*abd)
    i = 0
    while i < len(abd_n):
        if abd_n[i]+abd in nu:
            nu.remove(abd_n[i]+abd)
            
        i += 1
    print(f'{len_abd}:{ind}:{len(nu)}')
print(sum(nu))


print(f'Execution duration : {time.time() - start_time}')