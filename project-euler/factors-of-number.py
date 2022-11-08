from math_lib import generate_primes_range

fact = []

nu = [28,36]

primes = []

#print(primes)
#

def get_factors(n):
    startR = 3
    if n <= startR:
        print(f'min start values should be 4')
        return
    endR = int(n/2 + 1)
    primes = primes + generate_primes_range(startR,endR)
    #2 3 5 7 11 13
    factors = {1,n}
    print(primes)
    for p in primes:
        res = n
        count = 0
        print(f'{p}:{type(p)}')
        
        while res%p == 0:
            count = count + 1
            res = int(res/p)
            factors.add(p**count)
            factors.add(res)

    startR = endR
    print(f'divisors of {n}: {factors}')
