# Sum of prime number below a given number

limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
primes = [2]


def add_primes(num):
    global primes
    for i in range(3,num):
        sqRoot  = i**.5
        for p in primes:
            if i%p == 0:
                break
            if p >= sqRoot:
                primes.append(i)
                break
    return
add_primes(limitN)
print(f'Sum of prime numbers: {sum(primes)}')


