#Generate prime numbers below a given number


limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")
primes = [2]


def generate(num):
    global primes

    for i in range(3,num):
        sqRoot  = i**.5
        for p in primes:
            if i%p == 0:
                break
            if p >= sqRoot:
                primes.append(i)
                break
    return(primes)

generate(limitN)
print(f'Prime list: {primes}')


