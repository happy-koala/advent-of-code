#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()

one = []
two = []
sim = int()

for line in text.split('\n'):
#for line in example_text.strip().split('\n'):
    #print(line)
    one.append(int(line.split()[0]))
    two.append(int(line.split()[1]))

for num in one:
    sim += num * two.count(num)

print(f'sim : {sim}')