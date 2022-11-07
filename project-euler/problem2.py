# sum of even fibinoci value below given number

limitN = int(input("Enter limit Value:"))
print(f"Entered value is {limitN}")

fiblist = [1,2,3,5,8]
sum = 0
i = 2
prevFib = 1

while i < limitN:
    
    if i%2 == 0:
        sum = sum + i

    nextFib = i + prevFib
    prevFib = i
    i = nextFib

print(f'Sum of values is {sum}')
