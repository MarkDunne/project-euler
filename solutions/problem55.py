def rev(i): return int(str(i)[::-1])

sum = 0;
for i in range(10000):
    n = i + rev(i)
    for j in range(51):
        r = rev(n)
        if r == n:
            break
        n += r
    sum += int(j==50)

print(sum)
