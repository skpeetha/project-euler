import time

start_time = time.time()

alpha_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
p22file = open('G:\Srikanth\Python\project-euler\project-euler\p022_names.txt')
names_f = p22file.read().split(",")
names = []
#file.read().replace('"','').split(',')
for name in names_f:
    names += [name.strip('"')]
names = sorted(names)

total_sum = 0
i = 1
for name in names:
    name_sum = 0
    for c in name:
        name_sum += alpha_dict[c]
    total_sum += name_sum * i #instead of i, names.index(name)+1 can be used
    i += 1


print(total_sum)
p22file.close()

print(f'Execution duration : {time.time() - start_time}')