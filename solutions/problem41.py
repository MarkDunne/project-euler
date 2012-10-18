from time import clock
from itertools import permutations as perms

t = clock()
primes = set([2, 3])

pandsets = []
for n in range(2, 8):
    digits = range(1, n + 1)
    if not sum(digits) % 3 == 0:
        pandsets.append(digits)

primepands = set()
for pandset in pandsets:
    for perm in perms(pandset):
        n = int(''.join(str(num) for num in perm))
        flag = True
        for prime in primes:
            if n % prime == 0:
                flag = False
                break
        for div in range(max(primes), int(n ** 0.5) + 1, 2):
            if n % div == 0:
                primes.add(div)
                flag = False
                break
        if flag:
            primepands.add(n)
print(max(primepands))
print(clock() - t)