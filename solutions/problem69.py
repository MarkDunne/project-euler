from EulerUtils import genPrimes

primes = genPrimes(1000)

count = 1
for prime in primes:
	new = count * prime
	if new > 1000000:
		print count
		break
	else:
		count = new