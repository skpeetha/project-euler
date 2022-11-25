import time
from math_lib import generate_primes_range

start_time = time.time()
#limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
#print(f"Entered value is {limitN}")

lst = list(range(2,10**6))

big_count = 2
i = 0
while i < len(lst):
    count = 2
    n = lst[i]
    it = n
    while it/2 != 1:
        #print(it)
        if it%2 == 0:
            it = it/2
        else:
            it = 3*it + 1
        count = count + 1
        #if it in lst:
            #lst.remove(it)
    #print(n)
    #print(lst)
    
    if count > big_count:
        big_count = count
        print(f'Number: {n} Count: {big_count}')
    i = i + 1
    #quit()

print(f'Execution duration : {time.time() - start_time}')
