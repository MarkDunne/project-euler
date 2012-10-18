from EulerUtils import genPrimes

limit = 50000000
lim1 = limit ** 0.33
lim2 = limit ** 0.25
primes = genPrimes(int(limit ** 0.5))
cubes = [i ** 3 for i in primes if i < lim1]
fourths = [i ** 4 for i in primes if i < lim2]

P = set()
for a in primes:
	a = a ** 2 
	for b in cubes:
		b += a
		if b > limit: break
		for c in fourths:
			c += b
			if c >= limit: break
			P.add(c)
print len(P)