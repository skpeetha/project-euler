#largest prime factor ofa given number

limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")

sum = 0.0
i = 3

while limitN%2 == 0:
    limitN = limitN/2

while limitN/i != 1:
    
    if limitN%i == 0:
        limitN = limitN/i
    i = i + 2
    print(limitN)

print(f'Largest prime factor is {limitN}')
