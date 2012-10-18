from time import clock

def genPrimes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return set(['2'] + [str(i) for i in range(3,n,2) if sieve[i]])

goodDigits = set(['1','3','7','9'])
def goodNum(n):
    return not set(n) - goodDigits

t = clock()
count = 2
primes = set(filter(goodNum, genPrimes(1000000)))

for prime in primes:
    flag = True
    for i in range(len(prime)):
        prime = prime[1:] + prime[0]
        if not prime in primes:
            flag = False
            break
    if flag:
        count += 1
        
print(count, clock() - t)
