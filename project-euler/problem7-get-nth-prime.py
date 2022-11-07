# generate nth prime number
limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")
i = 3
count = 1
primes = [2]


def generate(num):
    global i
    global primes
    global count

    while count < num:
        for p in primes:
            if i%p == 0:
                break
            elif p == primes[-1]:
                primes = primes + [i]
                count = count + 1
        i = i + 2
    return(primes)
    
generate(limitN)
print(f'{limitN}th prime: {primes[-1]}')


