import os, math

def sum(n):
    return (n/2) * (2 + (n-1))

def numDivisors(n):
    divCount = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i ==0:
            divCount+=2
    return divCount


n = 1
maxDiv = 0;
while True:
    triN = sum(n)
    divs = numDivisors(triN)
    if(divs > maxDiv):
        maxDiv = divs
        print(str(maxDiv) + " - " + str(triN))
    n+=1

