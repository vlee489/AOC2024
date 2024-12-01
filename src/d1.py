from typing import List, Dict

left_row: List[int] = []
right_row: List[int] = []

with open('input/d1.txt', 'r') as file:
    for line in file:
        row = line.replace('\n', '').split('   ')
        left_row.append(int(row[0]))
        right_row.append(int(row[1]))

left_row = sorted(left_row)
right_row = sorted(right_row)

total_diff = 0

combined_list = list(zip(left_row, right_row))

for pair in combined_list:
    total_diff += abs(pair[0] - pair[1])

print(f"Part 1 Result: {total_diff}")

# Part 2

total_right_appeances: Dict[int, int] = {}
for left_num in set(left_row):  # Set is used for efficency, not like it matters
    total_right_appeances[left_num] = right_row.count(left_num)

similarity: int = 0

for left_num in left_row:
    similarity += left_num * total_right_appeances[left_num]

print(f"Part 2 Rsult: {similarity}")
