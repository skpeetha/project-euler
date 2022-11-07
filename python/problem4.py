# biggest palindrome when 2 n digit numbers are multiplied


def check_palindrome(num):
    if num[0] == num[-1]:
        i = 1
        length = len(num)
        #print(f'length:{length}:{num}')
        while i < length//2:
            if num[i] != num[-1-i]:
                return False
            i = i+1
        return True
    else:
        return False

i = 100
pal = 0
while i < 1000:
    j = 100
    while j < 1000:
        prod = i*j
        if check_palindrome(str(prod)) & (prod > pal):
            pal = prod
            print(f'pal:{pal}')
        j = j + 1
    i  = i + 1

print(f'MAx palindrome {pal}')
