from EulerUtils import genPrimes

lim = 1000000

sum = 0
sums = []
primes = genPrimes(lim)
for prime in primes:
    sum += prime
    if sum < lim:
        sums.append(sum)
    else:
        break

m, n = 0, 0
l = len(sums)
primes = set(primes) 
for i in range(l):
    for j in range(i + m, l):
        x = sums[j] - sums[i]
        if j - i > m and x in primes:
            n = x
            m = j - i
print m, n