import re

fh = open('regexp.txt')
lst = list()
for line in fh:
    x = re.findall('[0-9]+', line )
    lst = lst + x
lst1 = list()
add = 0
for i in lst:
    a = int(i)
    add = add + a

print(add)