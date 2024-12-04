from typing import List
import json

wordsearch: List[List[str]] = []
word = 'XMAS'
lookup_count = 0
xmas_count = 0
locations = []

with open('input/d4.txt', 'r') as file:
    for line in file:
        line_array = []
        for char in line.strip():
            line_array.append(char)
        wordsearch.append(line_array)


def check_location(row, collumn, direction: List[int], lookup_word):
    for word_char_loc in range(1, len(lookup_word)):
        row += direction[0]
        collumn += direction[1]
        if row < 0 or collumn < 0:
            return False
        if row >= len(wordsearch) or collumn >= len(wordsearch[row]):
            return False
        if not wordsearch[row][collumn] == lookup_word[word_char_loc]:
            return False
    return True


lookaround_values = [
    [-1, -1], [-1, 0], [-1, +1],
    [0, -1], [0, +1],
    [+1, -1], [+1, 0], [+1, +1]
]

first_char = word[0]
for y_index in range(len(wordsearch)):
    y_row = wordsearch[y_index]
    for x_index in range(len(y_row)):
        x_char = y_row[x_index]
        if x_char != first_char:
            continue
        check_results: List[bool] = [check_location(y_index, x_index, checks, word) for checks in lookaround_values]
        # print(check_results)
        if True in check_results:
            lookup_count += check_results.count(True)
            locations.append(f"{y_index}, {x_index}")

# Part 2
def check_xmas(row, collumn):
    check_locs = [
        [row - 1, collumn - 1], [row - 1, collumn + 1],
        [row + 1, collumn - 1], [row + 1, collumn + 1]
    ]
    for locs in check_locs:
        if locs[0] < 0 or locs[1] < 0:
            return False
        if locs[0] >= len(wordsearch) or locs[1] >= len(wordsearch[locs[0]]):
            return False
    for corners_index in [[0, 3], [1, 2]]:
        loc_1 = check_locs[corners_index[0]]
        loc_2 = check_locs[corners_index[1]]
        if not ((wordsearch[loc_1[0]][loc_1[1]] == 'M' and wordsearch[loc_2[0]][loc_2[1]] == 'S') or (
                    wordsearch[loc_1[0]][loc_1[1]] == 'S' and wordsearch[loc_2[0]][loc_2[1]] == 'M')):
            return False
    return True

for y_index in range(len(wordsearch)):
    y_row = wordsearch[y_index]
    for x_index in range(len(y_row)):
        x_char = y_row[x_index]
        if x_char != 'A':
            continue
        if check_xmas(y_index, x_index):
            xmas_count += 1

print(f"Part 1: {lookup_count}")
print(f"Part 2: {xmas_count}")
# print(locations)
