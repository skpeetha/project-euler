import time
from math_lib import generate_primes_range

start_time = time.time()

res = 2**1000
sum_n = 0
while res//10 != 0:
    sum_n = sum_n + res%10
    res = res//10
print(sum_n+res)

print(f'Execution duration : {time.time() - start_time}')