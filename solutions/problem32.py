from time import clock
from EulerUtils import isPandigital
  
def minY(x):
    return int(1000 / x)
    
def maxY(x):
    return int(10000 / x)

t = clock()
res = set()
for i in range(2, 100):
    for j in range(minY(i), maxY(i)):
        s = str(i) + str(j) + str(i * j)
        if isPandigital(s):
            res.add(i * j)
print sum(list(res)), clock() - t
        