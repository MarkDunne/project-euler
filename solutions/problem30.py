from time import clock
from itertools import combinations_with_replacement as combos

e = 5
t = clock()
total = -1
table = dict([(str(x), x ** e) for x in range(10)])
for combo in combos('0123456789', e + 1):
    squareSum = sum(table[n] for n in combo)
    if sorted(str(squareSum).zfill(e + 1)) == list(combo):
        total += squareSum
    
print(total, clock() - t)
