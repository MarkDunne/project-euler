#first python solution in thread to run under 1 second

from math import sqrt
from time import clock

t = clock()

lim = 20162
factorLim = int(sqrt(lim)) + 1
factors = dict([(x, set([1])) for x in range(1, lim)])

total = 0
abn = set()

def noSum():
    for a in abn:
        if n - a in abn:
            return False
    return True

for n in range(1, lim):
    if n < factorLim:
        for b in range(n, lim, n):
            factors[b].add(n)
            factors[b].add(int(b / n))
    if sum(factors[n]) > 2 * n:
       abn.add(n)
    if noSum():
        total += n

print(total, clock() - t)
