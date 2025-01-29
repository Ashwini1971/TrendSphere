import re
s = 'a3s2d4'
'output --> abcdstudefgh'
alpha = [i for i in s if i.isalpha()]
numbers = [i for i in s if i.isnumeric()]
print(alpha, numbers)
s_ = ''
for i, j in zip(alpha, numbers):
    for co in range(int(j)):
        s_ += ord(i) + 1











