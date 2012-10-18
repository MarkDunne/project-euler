def test(n):
    s = str(n * n)
    return s[0]=='1' and s[2]=='2' and s[4]=='3' and s[6]=='4' and s[8]=='5' and s[10]=='6' and s[12]=='7' and s[14]=='8' and s[16]=='9'

i, upper = 101010103, 138902658
while i < upper:
    if test(i):
        print str(i) + '0'
        break
    if test(i + 4):
        print str(i + 4) + '0'
        break
    i += 10