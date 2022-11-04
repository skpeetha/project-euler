
limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")

i = 5
primes = [2,3]
tempN = limitN
print(tempN)

while i <= limitN:
    #for p in primes:
    #    if i%p == 0:
    #        break
    #primes = primes + [i]
    j = 2
    while j < i:
        if i%j == 0:
            break
        j = j + 1
    else:
        primes = primes + [i]
    i = i + 1
    

print(f'Prime list: {primes}')

