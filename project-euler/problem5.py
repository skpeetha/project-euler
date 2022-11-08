from math import prod


ml = [16,9,5,7,11,13,17,19] #identified minimum multiples required
print(prod(ml))
quit()

#this is brute force takes lot of time
i = 20
while True:
    for m in range(1,20): #can use ml list instead of range
        if i%m != 0:
            break
        if m == 20:
            print(i)
            quit()
    i = i + 20