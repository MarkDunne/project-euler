from EulerUtils import isPrime, genPrimes
from time import clock

i, primes, total = 3, 0, 1

while True:
	d = i - 1
	p0 = i * i
	p1 = p0 - d
	p2 = p1 - d
	p3 = p2 - d

	total += 4
	primes += isPrime(p1) + isPrime(p2) + isPrime(p3)
	
	if primes * 10 < total:
		print i
		break

	i += 2