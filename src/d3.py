import re
import json

total_1 = 0
total_2 = 0
process_array = []

with open('input/d3.txt', 'r') as file:
    input_file = file.read()
    results = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_file)
    for mul in results:
        values = re.findall(r"\d{1,3}", mul)
        total_1 += (int(values[0]) * int(values[1]))

    results = ['do()'] + re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input_file)
    processing_row = []
    include_mul = True
    for result in results:
        if result == 'do()':
            include_mul = True
        elif result == "don't()":
            include_mul = False
        elif include_mul:
            process_array.append(result)

    for mul in process_array:
        values = re.findall(r"\d{1,3}", mul)
        total_2 += (int(values[0]) * int(values[1]))


print(f"Part 1: {total_1}")
print(f"Part 2: {total_2}")
