from math import sqrt
from math import floor
from time import clock

def getHex(index):
    return index * (2 * index - 1)

def isPent(n):
    return isNat((sqrt(24 * n + 1) + 1) / 6)

def isTri(n):
    return isNat((sqrt(8 * n + 1) - 1) / 2)

def isNat(n):
    return floor(n) == n


t = clock()
n = 144
while(True):
    h = getHex(n)
    if(isPent(h)):
       print(h, n)
       break
    n+=1

print(clock() - t)
