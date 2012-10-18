from math import log10

p, q, t = 3, 2, 0
for i in range(1000):
    if int(log10(p)) > int(log10(q)):
        t += 1
    p, q = p + 2 * q, p + q
print(t)
