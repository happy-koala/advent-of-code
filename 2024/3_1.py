#!/usr/bin/env python3

import sys
import re

text = open(sys.argv[1]).read().strip()

instructions = re.findall(r"mul\(\d+,\d+\)", text)

result = 0

for i in instructions:
    x, y = map(int, re.sub("[^0-9,]","",i).split(','))
    result += x*y

print(f"result {result}")