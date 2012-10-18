import string
from time import clock
from itertools import permutations as perms

t = clock()
data = eval(open("data/cipher1.txt").read())
chars = dict([(ord(c), c) for c in string.printable])
keys = set(perms(range(61, 123), 3))


sols = []
l = range(len(data))
for key in keys:
    text = []
    flag = True
    for i in l:
        c = data[i] ^ key[i % 3]
        if c not in chars:
            flag = False
            break
        else:
            text.append(chars[c])
    if flag:
        text = ''.join(text)
        if ' the ' in text:
            sols.append(key)

if len(sols) == 1:
    print(sum([data[i] ^ sols[0][i % 3] for i in l]))
    print(clock() - t)
