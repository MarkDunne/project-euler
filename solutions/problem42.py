from string import ascii_uppercase
from time import clock

t = clock()
words = eval(open("words.txt").read())
ascii_table = ascii_uppercase
tri_table = [0.5 * n * (n + 1) for n in range(1, 27)]

count = 0
for word in words:
    if(sum(ascii_table.index(char) + 1 for char in list(word)) in tri_table):
       count += 1
print(count)
print(clock() - t)


