n = 1
degree = 6
while True:
    flag = True
    s = sorted(str(n))
    for mul in range(2, degree + 1):
        if not s == sorted(str(n * mul)):
            flag = False
            break
    if flag:
        print(n)
        break
    n += 1