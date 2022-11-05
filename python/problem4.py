# biggest palindrome when 2 n digit numbers are multiplied

limitN = input("Enter numerical limit value:")
print(f"Entered value is {limitN}")

length = len(limitN)
print(f'length:{length}')
i= 0
while i > length/2:
     if limitN[0] != limitN[-1-i]:
         print(f'not palindrome')
         exit
     i = i+1
     print(f'in loop')
     

print(f'Sum of values is ')
