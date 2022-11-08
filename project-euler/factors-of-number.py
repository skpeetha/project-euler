from math_lib import generate_primes_range

fact = []

nu = [28,36]

primes = [2]

#print(generate_primes_range(5,15))

#quit()
startR = 2
if nu[0] <= startR:
    print(f'min start values should be 4')
    quit()

for n in nu:
    endR = int(n/2 + 1)
    primes = primes + generate_primes_range(startR,endR)
    #2 3 5 7 11 13
    factors = {1,n}
    print(primes)
    for p in primes:
        res = n
       # print(f'{p}:{type(p)}')
        count = 0
        while res%p == 0:
            res = int(res/p)
            count = count + 1
            factors.add(p**count)
            factors.add(res)
        if res/p == 1.0:
            break
    startR = endR
    print(f'divisors of {n}: {factors}')
