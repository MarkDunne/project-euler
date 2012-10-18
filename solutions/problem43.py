from time import clock
t = clock()
digits = set('123456789')
divs = [3,5,7,11,13,17]
joins = set()

for x in range(1000, 10000, 2):
    x = str(x)
    if len(set(x)) == len(x):
        joins.add(x)
        
for div in divs:
    temp = []
    for j in joins:
        for d in digits - set(j):
            n = j + d
            if int(n[-3:]) % div == 0:
                temp.append(n)
    joins = temp
  
print(sum(map(int, joins)), clock() - t)
                
