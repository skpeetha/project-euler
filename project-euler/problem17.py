# sum of letters of first 1000 numbers
num_lts = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
tens_lts = {1:3,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
hundred = 7
thousand = 8
ad = 3

n = 1
total_let = num_lts[1] + thousand
while n < 1000:
    if n%100 != 0:
        #total_let += ad
        if n%100 < 20:
            total_let += num_lts[n%100]
        else:
            total_let += tens_lts[(n%100)//10] + num_lts[n%10]
    print(total_let)
    if n//100 != 0:
        total_let += num_lts[n//100] + hundred
        if n%100 != 0:
            total_let += ad
    n += 1
    #break
print(total_let)

