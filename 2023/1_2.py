#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()

liste = []
sum = 0

for line in text.split('\n'):
    nums = []
    for c, l in enumerate(line):
        if l.isdigit():
            nums.append(l)
        else:
            for k, v in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[c:].startswith(v):
                    nums.append(str(k+1))
    sum += int(nums[0] + nums[-1])
    #print(nums)

print(f'sum : {sum}')