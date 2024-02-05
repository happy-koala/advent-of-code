#!/usr/bin/env python3

import sys

data = open(sys.argv[1]).read().strip()
cubes = {'red': 12, 'green': 13, 'blue': 14}

ids = []
sum = 0

for i in data.strip().split('\n'):
    worx = True
    k, v = i.split(':')
    id = k.split(' ')[1]
    for game in v.strip().split(';'):
        if worx == False:
            break
        cubes_shown = [c.strip() for c in game.split(',')]
        for p in cubes_shown:
            digit, color = p.split(' ')[0], p.split(' ')[1]
            if cubes[f'{color}'] < int(digit):
                worx = False
                break
    ids.append(id) if worx == True else None
    if worx == True:
        sum += int(id)

ids = [int(i) for i in ids]

print(f'sum : {sum}')