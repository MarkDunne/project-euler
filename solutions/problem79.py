from collections import defaultdict
digits = defaultdict(int)
for key in set(open('data/keylog.txt').read().split()):
    s = 0
    for i, c in enumerate(key):
        digits[c] += s + i
        s = digits[c]        
print ''.join(sorted(digits, key=digits.get))