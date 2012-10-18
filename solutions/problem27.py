from EulerUtils import genPrimes

primes = set(genPrimes(1000))

m, x, y = 1, 0, 0
for a in range(-999, 0, 2):
    for b in primes:
        n, res = 1, 2
        while res in primes:            
            res = n ** 2 + a * n + b
            if n > m:
                m, x, y = n, a, b
            n += 1
print x * y