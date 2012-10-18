from math import floor
from math import sqrt

def genPrimes(n):
    #http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def isPrime(n):
    if n == 2 or n == 3: 
        return True
    if n < 2 or n % 2 == 0: 
        return False
    if n < 9: 
        return True
    if n % 3 == 0: 
        return False
    factor, lim = 5, int(sqrt(n))
    while factor < lim:
        if n % factor == 0: 
            return False
        if n % (factor + 2) == 0: 
            return False
        factor +=6
    return True
  
def numDivs(x):
    #http://en.wikipedia.org/wiki/Formula_for_primes
    divs = 0
    for s in range(1, int(sqrt(x))):
        divs += floor(x / s) - floor((x - 1) / s)
    return int(2 * divs)
    
def isPandigital(n, l = 9): 
    n = str(n)
    return len(n) == l and not '1234567890'[:l].strip(n) 

def digitsToNum(nums):
    return int(''.join(map(str, nums)))
    
def polygonArea(pts):
    s = 0
    for i in range(len(pts) - 1):
        s += pts[i][0] * pts[i + 1][1] - pts[i+1][0] * pts[i][1]
    return abs(s) / 2
