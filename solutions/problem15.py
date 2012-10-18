def init():
        print(getPascalTerm(2 * 3 ,3))

def getPascalTerm(row, term):
        return fact(row) / ( fact(term) * fact(row - term) )


def fact(n):
	if(not n <= 1):
		return n * fact(n - 1)
	else:
		return 1;

init();
