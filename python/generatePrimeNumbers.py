# generate prime number below a given number
limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")
i = 5
primes = [2,3]


def generate(num):
    global i
    global primes

    while i <= num:
        for p in primes:
            if i%p == 0:
                break
            elif p == primes[-1]:
                primes = primes + [i]
    return(primes)
    #primes = primes + [i]
    #j = 2
    #while j < i:
    #    if i%j == 0:
    #        break
    #    j = j + 1
    #else:
    #    primes = primes + [i]
        i = i + 2
generate(limitN)
print(f'Prime list: {primes}')

