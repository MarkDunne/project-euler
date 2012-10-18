from time import clock
from math import sqrt
from math import acos

def angVectors(a, b):
    normA = sqrt(a[0] ** 2 + a[1] ** 2)
    normB = sqrt(b[0] ** 2 + b[1] ** 2)
    ang = (a[0] * b[0] + a[1] * b[1]) / (normA * normB)
    return acos(ang)
  
s, t = 0, clock()
for line in file("data/triangles.txt"):
    pts = eval(line)
    a, b, c = (pts[0], pts[1]), (pts[2], pts[3]), (pts[4], pts[5])

    xpts = [pts[0], pts[2], pts[4]]
    ypts = [pts[1], pts[3], pts[5]]  
    ang = angVectors(a, b) + angVectors(b, c) + angVectors(c, a)
    if str(ang)[:5] == "6.283":
        s += 1
print s, clock() - t