import time
from math_lib import generate_primes_range

start_time = time.time()

cur = 1
nex = 1
l = len(str(nex))
ind = 2
while l < 1000:
    temp = nex
    nex += cur
    ind += 1
    cur = temp
    l = len(str(nex))
    #if t > l:
    #    print(t)
    #l = t
print(ind)
print(f'Execution duration : {time.time() - start_time}')