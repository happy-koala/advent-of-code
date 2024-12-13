#!/usr/bin/env python3

import sys
import math 

text = open(sys.argv[1]).read().strip()
rules = text.strip().split('\n\n')[0].split('\n')
updates = text.strip().split('\n\n')[1].split('\n')

mp_nums = []
incorrect_u = []

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
        continue
    else:
        incorrect_u.append(update)

corrected_updates = []

for update in incorrect_u:
    check = False
    round = 0
    while check is False:
        checks = []
        for page_index, page in enumerate(update[:-1]):
            rule_check = f"{page}|{update[page_index+1]}"
            rule_check_rev = f"{update[page_index+1]}|{page}"
            if rule_check in rules:
                checks.append(True)
            elif rule_check_rev in rules:
                checks.append(False)
                update[page_index+1], update[page_index] = update[page_index], update[page_index+1]
        round += 1
        if len(checks) > 0 and all(checks):
            check = True
            corrected_updates.append(update)

mp_nums_sum = 0

for update in corrected_updates:
    m_num_pos = math.floor(len(update)/2)
    mp_nums_sum += int(update[m_num_pos])

print(mp_nums_sum)
