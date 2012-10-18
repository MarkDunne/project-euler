from itertools import count
from time import clock

lim = 6
seen = {}
t = clock()

for i in count(2, 1):
    p = pow(i, 3)
    s = ''.join(sorted(str(p)))
    if s in seen:
        seen[s][0] += 1
        if seen[s][0] == lim:
            print seen[s][1], clock() - t
            break
    else:
        seen[s] = [1, p]