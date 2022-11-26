from math import factorial
import time

start_time = time.time()

n = 100
prd = 1

while n > 0: #print(factorial(n))
    prd  = prd * n
    n -= 1
print(sum(int(digit) for digit in str(prd)))


print(f'Execution duration : {time.time() - start_time}')