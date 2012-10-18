def digitalSum(n):
    return sum(map(int, list(str(n))))

m = 0
for a in range(90, 100):
    for b in range(90, 100):
        s = digitalSum(pow(a, b))
        if s > m:
            m = s
print m