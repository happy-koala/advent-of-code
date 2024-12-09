#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()
lines = text.strip().split('\n')
strings = []

for i_line, line in enumerate(text.strip().split('\n')):
    strings.append(line)
    strings.append(line[::-1])
    if i_line == 0:
        for i_char, char in enumerate(line[1:]):
            diagonal = ''
            start_line = i_line
            for n in range(i_char,len(line)-1):
                diagonal += lines[start_line][n+1]
                start_line += 1
            if len(diagonal) >= 4:
                strings.append(diagonal)
                strings.append(diagonal[::-1])
            else:
                None
        for i_char, char in enumerate(line[1:]):
            diagonal = ''
            start_line = i_line
            for n in range(i_char,len(line)-1):
                diagonal += lines[start_line][::-1][n+1]
                start_line += 1
            if len(diagonal) >= 4:
                strings.append(diagonal)
                strings.append(diagonal[::-1])
            else:
                None
    diagonal = ''
    start = i_line
    for i in range(0,min(len(lines)-i_line, len(line))):
        diagonal += lines[start][i]
        start += 1
    if len(diagonal) >= 4:
        strings.append(diagonal)
        strings.append(diagonal[::-1])
    else:
        None
    diagonal = ''
    start = i_line
    for i in range(0,min(len(lines)-i_line, len(line))):
        diagonal += lines[start][::-1][i]
        start += 1
    if len(diagonal) >= 4:
        strings.append(diagonal)
        strings.append(diagonal[::-1])
    else:
        None

for i_char, _ in enumerate(line):
    vertical = ''
    for line in lines:
        vertical += line[i_char]
    strings.append(vertical)
    strings.append(vertical[::-1])
        
total_count = sum(s.count("XMAS") for s in strings)
print(total_count)