from time import clock
from math import factorial as fact

def getCombos(n, r):
    return fact(n) / (fact(r) * (fact(n - r)))

t = clock()
c = 0
for n in range(1, 101):
    lim = n / 2 + 1
    if n % 2 == 0:
        
    for r in range(1, lim):
        if getCombos(n, r) > 1000000:
            c += 2
print c, clock() - t
        