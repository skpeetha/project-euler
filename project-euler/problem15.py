# total paths from left top corner to right bottam corner in 20x20 grid

import time
from math_lib import generate_primes_range

start_time = time.time()

rows = list(range(3))
colms = list(range(3))

for r in rows:
    for c in colms:
        print(r,c)

print(f'Execution duration : {time.time() - start_time}')
