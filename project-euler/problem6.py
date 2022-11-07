#Difference of sum of square of sum of numbers and sum of squares of each number
limitN = int(input("Enter numerical limit value:")) # fails if enetred value is not a number
print(f"Entered value is {limitN}")

n = limitN
sum_of_num = n*(n+1)/2
i=1
sum_of_sq = 0
while i <= limitN:
    sum_of_sq = sum_of_sq + i*i
    i = i + 1
diff  = sum_of_num*sum_of_num - sum_of_sq
print(f'Difference of sums is {diff}')
