#!/usr/bin/env python3

import sys

data = open(sys.argv[1]).read().strip()
cubes = {'red': 12, 'green': 13, 'blue': 14}

sum = 0

for i in data.strip().split('\n'): 
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    power = []
    k, v = i.split(':')
    for game in v.strip().split(';'):
        cubes_shown = [c.strip() for c in game.split(',')]
        for p in cubes_shown:
            digit, color = p.split(' ')[0], p.split(' ')[1]
            if cubes[f'{color}'] < int(digit):
                cubes[f'{color}'] = int(digit)
    sum += cubes['red'] * cubes['green'] * cubes['blue']

print(f'sum : {sum}')