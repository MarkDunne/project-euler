from time import clock
from math import sqrt

def isPent(n):
    x = (sqrt(24 * n + 1) + 1) / 6
    return int(x) == x

def wrapper():
    i = 2
    pents = [1]
    pentsset = set([1])
    while True:
        a = (3 * i * i - i) / 2
        pents.append(a)
        pentsset.add(a)
        for j in range(1, i):
            b = pents[j]
            if (a - b) in pentsset and isPent(a + b):
                return a - b
        i += 1

t = clock()
print wrapper(), clock() - t