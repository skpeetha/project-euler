#special pythogarem triplet
abc = 0
for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if (a*a + b*b == c*c) & (a+b+c == 1000):
                abc = a*b*c
                print(f'{a}:{b}:{c}')
                break
        if abc != 0:
            break
    if abc != 0:
        break
print(f'{abc}')