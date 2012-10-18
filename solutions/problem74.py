from time import clock
from itertools import combinations_with_replacement as combos
from collections import defaultdict

target = 60

fact = {0:1}
for i in range(1, 10):
    fact[i] = fact[i - 1] * i

def fact_sum(n):
    s = 0
    while n:
        s += fact[n%10]
        n /= 10
    return s
    
def appearences(n):
    s = list(set(n))
    x = fact[len(n)]
    for c in s:
        x /= fact[n.count(c)]
    return x

t = clock()
count = 0
chains = defaultdict(int)
for n in combos('0123456789', 6):
    o = n = int(''.join(n))
    chain, chain_len = [], 0
    while True:
        if chains[n] == 0:
            chains[n] = None
            chain_len += 1
            chain.append(n)
        else:
            if chains[n]:
                chain_len += chains[n]
            break
        n = fact_sum(n)
    
    if chain_len == target:
        o = str(o)
        if '1' in o: 
            count += 2 * appearences(o) - fact[len(o) - 1]
        else:
            count += appearences(o)

    for i in chain:
        chains[i] = chain_len
        chain_len -= 1

print count, clock() - t