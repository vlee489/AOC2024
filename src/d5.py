from math import floor
from typing import List
from graphlib import TopologicalSorter

rules: List[List[int]] = []
orders: List[List[int]] = []
incorrect_order: List[List[int]] = []
middle_total: int = 0
corrected_middle_total: int = 0

with open('input/d5.txt', 'r') as file:
    for line in file:
        if "|" in line:
            split = line.split('|')
            rules.append([int(split[0]), int(split[1])])
        elif ',' in line:
            split = line.split(',')
            orders.append([int(v) for v in split])

def check_order(p_order: List[int]) -> bool:
    for loc in range(len(p_order)):
        val = p_order[loc]
        for rule in rules:
            if val in rule:
                val_index = rule.index(val)
                other_val = rule[val_index - 1]
                if not other_val in p_order:
                    continue
                val_order = p_order.index(val)
                other_val_order = p_order.index(other_val)
                if not (((val_index == 0) and (val_order < other_val_order)) or (
                        (val_index == 1) and (val_order > other_val_order))):
                    return False
    return True

def correct_order(p_order: List[int]) -> List[int]:
    ts = TopologicalSorter()
    for rule in rules:
        if rule[0] in p_order and rule[1] in p_order:
            ts.add(rule[0], rule[1])
    return [*ts.static_order()]

for order in orders:
    if check_order(order):
        middle_total += (order[floor((len(order) - 1) / 2)])
    else:
        incorrect_order.append(order)
for order in incorrect_order:
    new_order = correct_order(order)
    corrected_middle_total += (new_order[floor((len(new_order) - 1) / 2)])

print(f"Part 1: {middle_total}")
print(f"Part 2: {corrected_middle_total}")
