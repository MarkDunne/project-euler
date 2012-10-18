from time import clock
from math import ceil
from math import log10
from EulerUtils import genPrimes

primes = genPrimes(100)

def up(n):
    return int(ceil(n))  

l = len(primes)
def sol(i, pLim):
    s = 0
    if i == len(primes):
        return 1
    else:
        p = primes[i]
        r = log10(p)
        lim = up((9 - pLim) / r)
        for x in range(lim):            
            s += sol(i + 1, pLim + x * r)
        return s
 
t = clock()   
print sol(0, 0) + 1
print clock() - t
                