import time
from math_lib import generate_primes_range

start_time = time.time()

limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")

print(f'Execution duration : {start_time - time.time()}')