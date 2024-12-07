from typing import List

floor_map: List[List[str]] = []

direction_moves = {
    "UP": [-1, 0],
    "DOWN": [1, 0],
    "RIGHT": [0, 1],
    "LEFT": [0, -1]
}

direction_change = {
    "UP": "RIGHT",
    "RIGHT": "DOWN",
    "DOWN": "LEFT",
    "LEFT": "UP"
}

def out_of_bounds_check(r, c) -> bool:
    """
    returns false when out of bounds
    """
    if r < 0 or r >= len(floor_map):
        return False
    if c < 0 or c >= len(floor_map[r]):
        return False
    return True

with open('input/d6.txt', 'r') as file:
    for line in file:
        row = []
        line = line.strip('\n')
        for char in line:
            row.append(char)
        floor_map.append(row)

direction = 'UP'
guard_loc_row, guard_loc_collumn = 0, 0
for row in range(len(floor_map)):
    for collumn in range(len(floor_map[row])):
        if floor_map[row][collumn] == '^':
            guard_loc_row, guard_loc_collumn = row, collumn
            floor_map[guard_loc_row][guard_loc_collumn] = 'X'

while True:
    move_dir = direction_moves[direction]
    if not out_of_bounds_check(guard_loc_row+move_dir[0], guard_loc_collumn+move_dir[1]):
        break
    match floor_map[guard_loc_row+move_dir[0]][guard_loc_collumn+move_dir[1]]:
        case '#':
            direction = direction_change[direction]
        case '.' | 'X':
            floor_map[guard_loc_row+move_dir[0]][guard_loc_collumn+move_dir[1]] = 'X'
            guard_loc_row = guard_loc_row+move_dir[0]
            guard_loc_collumn = guard_loc_collumn+move_dir[1]

print(f"Part 1: {[j for sub in floor_map for j in sub].count('X')}")
