import time
from math_lib import generate_primes_range

start_time = time.time()

def get_length(f):
    l = len(f)
    if l == 1:
        return "0"
    ind = 0
    for s in f:
        if s != "0":
            ind = f.index(s)
            break
    i = ind
    step = ind
    while i < l:        
        if f[:i] == f[i:i+step]:
            return f[:i]
        else:
            step += 1
        i += 1
        if (i+step > l):
            return "0"

ma = 0
for n in range(2,1000):
    f = get_length(str("%.1000f"%(1/n))[2:].rstrip('0'))
    l = len(f)
    if ma < l:
        ma = l
        print(f'decimal: {f} len: {l} num: {n}')
    #print(f'decimal: {f} len: {l} num: {n}')
print(ma)
print(f'Execution duration : {time.time() - start_time}')