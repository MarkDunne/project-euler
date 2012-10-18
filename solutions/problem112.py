from time import clock

def bouncy(n):
    inc, dec = False, False
    n, last = divmod(n, 10)
    while not n == 0:
        n, next = divmod(n, 10)
        if next > last: 
            inc = True
        elif next < last: 
            dec = True
        if inc and dec: 
            return True
        last = next
    return False

c, i, t = 0.0, 99, clock()
while True:
    i += 1
    if bouncy(i):
        c += 1
        if c / i >= 0.99:
            print i
            break

print clock() - t