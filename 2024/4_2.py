#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()
lines = text.strip().split('\n')

lines_inner = lines[1:-1]
strings = []
count = 0

for i_line, line in enumerate(lines_inner):
    for i_char, char in enumerate(line[1:-1]):
        if char == 'A':
            diag_1 = lines[i_line][i_char] + char + lines[i_line+2][i_char+2]
            diag_2 = lines[i_line+2][i_char] + char + lines[i_line][i_char+2]
            if diag_1 in {'MAS', 'SAM'} and diag_2 in {'MAS', 'SAM'}:
                count += 1

print(count)