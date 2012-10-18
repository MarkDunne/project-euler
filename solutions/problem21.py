import math

def sumOfDivs(n):
    sum = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            sum = sum + i + n / i
    return sum - n
        

sum = 0
for i in range(1, 10001):
    a = sumOfDivs(i)
    if(not a == i):
        if(sumOfDivs(a) == i):
            sum += i

print(sum)
