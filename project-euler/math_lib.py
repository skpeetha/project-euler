#Generate prime numbers below a given number


#limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
#print(f"Entered value is {limitN}")
#primes = [2]


def generate_primes(num):
    #global primes
    primes = [2]

    for i in range(3,num):
        sqRoot  = i**.5
        for p in primes:
            if i%p == 0:
                break
            if p >= sqRoot:
                primes.append(i)
                break
    return(primes)

def generate_primes_range(startR,endR):
    #global primes
    primes_start = generate_primes(startR)
    primes = []

    for i in range(startR,endR):
        sqRoot  = i**.5
        for p in primes_start:
            if i%p == 0:
                break
            if p >= sqRoot:
                primes.append(i)
                primes_start.append(i)
                break
    return(primes)

#print(generate_primes_range(4,10))


