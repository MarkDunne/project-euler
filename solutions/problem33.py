#much better solutions possible

from time import clock
from fractions import gcd
from itertools import product
from EulerUtils import genPrimes

t = clock()
primes = genPrimes(100)
pn, pd = 1, 1
for n in range(10, 100):
    for d in range(n + 1, 100):
        
        if n % 10 == 0 or d % 10 == 0:
            continue
        
        n, d = float(n), float(d)                
        ns, ds = str(n), str(d)  
        
        for row in product((0, 1), (0, 1)):
            a, b = row
            if ns[a] == ds[b]:
                if float(ns[1 - a]) * d == float(ds[1 - b])  * n:
                    pn, pd = pn * n, pd * d

print pd / gcd(pn, pd), clock() - t