#!/usr/bin/env python3

import sys
import math 

text = open(sys.argv[1]).read().strip()
rules = text.strip().split('\n\n')[0].split('\n')
updates = text.strip().split('\n\n')[1].split('\n')

mp_nums = []

for i, update in enumerate(updates):
    checks = []
    update = update.split(',')
    for rule in rules:
        rule = rule.split('|')
        pos_1 = update.index(rule[0]) if rule[0] in update else float('inf')
        pos_2 = update.index(rule[1]) if rule[1] in update else float('inf')
        if rule[0] in update and rule[1] in update and update.index(rule[0]) >= update.index(rule[1]):
            checks.append(False)
        else:
            checks.append(True)
    if all(checks):
        m_num_pos = math.floor(len(update)/2)
        mp_nums.append(update[m_num_pos])

total = sum(map(int, mp_nums))
print(total)