from itertools import permutations as perms

digits = [9, 8, 7, 6, 5, 4, 3, 2, 1]
pands = perms(digits)

def digitsToNum(nums):
    return ''.join(map(str, nums))
  
for i in range(1, 5):
    n = "192384576"
    div, n = int(n[:i]), n[i - 1:]
    check = str(2 * div)
    while n[i:].find(check) == 0:
        print div
            
       
    