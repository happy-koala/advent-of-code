#!/usr/bin/env python3

import sys

text = open(sys.argv[1]).read().strip()

count = 0

for report in text.strip().split('\n'):
    report = report.split()
    report_ext = [report] + [report[:i] + report[i + 1:] for i in range(len(report))]
    for elem in report_ext:
        levels = list(map(int, elem))
        diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

        if any(abs(diff) < 1 or abs(diff) > 3 for diff in diffs):
            continue
        elif not (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)):
            continue
        else: 
            count += 1
            break

print(f"count {count}")