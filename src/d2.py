safe_reports: int = 0
bad_reports: int = 0

with open('input/d2.txt', 'r') as file:
    for line in [line.rstrip('\n') for line in file]:
        line = [int(num) for num in line.split(' ')]

        valid_line: bool = True
        direction: str = 'neither'
        if line[0] < line[1]:
            direction = 'up'
        elif line[0] > line[1]:
            direction = 'down'

        if direction == 'neither':
            bad_reports += 1
            pass

        for num_index in range(0, len(line)-1):
            # print(f"{num_index}:{line[num_index]}:{abs(line[num_index]-line[num_index+1])}")
            if 1 <= abs(line[num_index]-line[num_index+1]) <= 3:
                if not ((line[num_index] > line[num_index+1] and direction == 'down') or (line[num_index] < line[num_index+1] and direction == 'up')):
                    valid_line = False
            else:
                valid_line = False

        if valid_line:
            print('passed')
            safe_reports += 1
        else:
            print('failed')
            bad_reports += 1

print(f"Bad reports: {bad_reports}")
print(f"Safe reports: {safe_reports}")


# My day 2 solution is so bad i've not commited it >.<
