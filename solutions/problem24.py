from itertools import permutations
results = list(permutations('0123456789'))
print(''.join(results[1000000 - 1]))
