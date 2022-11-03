
totalnumbers =int(input("Enter limit value:\n"))
sum  = 0.0
i = 3
while i < totalnumbers:
    # possible better solutions
    # merge both conditions with or in a single conidtion
    # find and add only multipliers of 3 and 5 Ex: i*3 & i*5 i < 350 (approx 1000/3 exact value 333)
    if i%3 == 0:
        sum = sum + i
    elif i%5 == 0:
        sum = sum + i

    i = i + 1
    print(sum)
print(sum)
