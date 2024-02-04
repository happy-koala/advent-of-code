#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()

liste = []

for line in text.split('\n'):
    one = ''
    two = ''
    for j in line:
        if j.isdigit():
            one = j
            break
    for k in line[::-1]:
        if k.isdigit():
            two = k
            break
    liste.append([one, two])

sum = 0
for i in liste:
    val = int(i[0]+i[1])
    #print(val)
    sum += val

print(f'sum : {sum}')