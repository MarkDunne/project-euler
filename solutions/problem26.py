from time import clock
from EulerUtils import genPrimes

t = clock()
primes = genPrimes(1000)[3:]
pows = [10 ** i for i in range(1, 1000)]

m, n = 0, 0
for d in primes:
    p = [i for i in pows if (i - 1) % d == 0][0]
    if p > m:
        m, n = p, d
print clock() - t, n