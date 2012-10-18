d = {0:1, 1:2}

def b(n):
	if n % 3 == 0:
		return 2 * n / 3
	else:
		return 1

def P(n):		
        if n in d:
                return d[n]
        else:
                d[n] = b(n) * P(n - 1) + P(n - 2)
                return d[n]

print sum([int(c) for c in str(P(100))])
