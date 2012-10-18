from time import clock
from EulerUtils import genPrimes

t = clock()
primes = set(genPrimes(10000))
for prime in primes:
    if 1000 < prime < 3340:
        a = prime + 3330
        b = prime + 6660
        if a in primes and b in primes:
            if set(str(prime)) == set(str(a)) == set(str(b)):
                print str(prime) + str(a) + str(b), clock() - t
    