from math import floor

def binIsPal(n):
    collector = []
    while(not n == 0):
        collector.append(str(n % 2))
        n = floor(n / 2)
    return collector == collector[::-1]

def isPal(pal):
    return pal == pal[::-1]

palSum = 0
for n in range(1, 1000000, 2):
    if(isPal(str(n)) and binIsPal(n)):
        print(n)
        palSum += n

print(palSum)
