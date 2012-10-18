from math import log
from time import clock
m, lnM, t = 0, 0, clock()
for ln, line in enumerate(file("data/base_exp.txt")):
    line = eval(line)
    dCount = line[1] * log(line[0])
    if dCount > m:
        m, lnM = dCount, ln
print lnM, clock() - t