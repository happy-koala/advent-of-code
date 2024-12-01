#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()

one = []
two = []
dist = int()

for line in text.split('\n'):
    one.append(int(line.split()[0]))
    two.append(int(line.split()[1]))

one.sort()
two.sort()

for c, v in enumerate(one):
    dist += abs(v-two[c])

print(f'dist : {dist}')

