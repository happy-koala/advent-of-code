#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()

count = 0

for report in text.strip().split('\n'):
    levels = list(map(int, report.split()))  
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]  
    
    if any(abs(diff) < 1 or abs(diff) > 3 for diff in diffs):
        continue
    if not (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)):
        continue
    
    count += 1

print(f"count: {count}")