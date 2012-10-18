from math import sqrt
from time import clock

t = clock()

primes = [2, 3, 5, 7]
i = 9
while True:
    isPrime = True
    solExists = False    
    for p in primes:
        if isPrime:
            isPrime = i % p
        if not solExists:
            n = sqrt((i - p) / 2)
            if int(n) == n:
                solExists = True
                break
    if not isPrime and not solExists:
        print i, clock()- t
        break
    if isPrime:
        primes.append(i)                
    i += 2