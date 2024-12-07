from typing import List, TypedDict

class Calibration(TypedDict):
    total: int
    values: List[int]

calibration_values: List[Calibration] = []
part_1_total = 0
part_2_total = 0

with open('input/d7.txt', 'r') as file:
    for line in file:
        part = line.split(': ')
        calibration_values.append({
            "total": int(part[0]),
            "values": [int(x) for x in part[1].split(' ')]
        })

def part_1_check(input_val: List[int], c_values: List[int], n: int, target: int) -> List[int]:
    if n >= len(c_values):
        return input_val
    check_val = c_values[n]
    return_vals: List[int] = []
    for i in input_val:
        return_vals.append(i * check_val)
        return_vals.append(i + check_val)
    return_vals = [v for v in return_vals if v <= target]
    return part_1_check(return_vals, c_values, n+1, target)

def part_2_check(input_val: List[int], c_values: List[int], n: int, target: int) -> List[int]:
    if n >= len(c_values):
        return input_val
    check_val = c_values[n]
    return_vals: List[int] = []
    for i in input_val:
        return_vals.append(i * check_val)
        return_vals.append(i + check_val)
        return_vals.append(int(f"{i}{check_val}"))
    return_vals = [v for v in return_vals if v <= target]
    return part_2_check(return_vals, c_values, n+1, target)

for c in calibration_values:
    checked_values_p1 = part_1_check([c['values'][0]], c['values'], 1, c['total'])
    checked_values_p2 = part_2_check([c['values'][0]], c['values'], 1, c['total'])
    # print(f"{c['total']} : {checked_values_p1}")
    if c['total'] in checked_values_p1:
        part_1_total += c['total']
    if c['total'] in checked_values_p2:
        part_2_total += c['total']

print(f"Part 1: {part_1_total}")
print(f"Part 2: {part_2_total}")