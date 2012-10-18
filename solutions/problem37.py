from time import clock
from math import log10
from itertools import permutations as perms

def isSol(pand):
    for i in range(1, 5):
        n = pand
        div, n = int(n[:i]), n[i:]
        mul = 2 * div
        while n.find(str(mul)) == 0:
            mul += div
            n = n[int(log10(mul)) + 1:]
            if not n:
                return True 
    return False
  
t = clock()  
pands = perms(['9','8','7', '6', '5', '4', '3', '2', '1'])
for pand in pands:
    pand = ''.join(pand)
    if isSol(pand):
        print pand, clock() - t
        break
