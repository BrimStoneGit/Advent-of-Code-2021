horizontal_pos = 0
depth = 0
aim = 0
for line in open("puzzle_input.txt"):
    cmd = line
    splitted_cmd = cmd.split(' ')
    if splitted_cmd[0] == 'forward':
        horizontal_pos += int(splitted_cmd[1])
        depth += aim * int(splitted_cmd[1])
    elif splitted_cmd[0] == 'down':
        aim += int(splitted_cmd[1])
    elif splitted_cmd[0] == 'up':
        aim -= int(splitted_cmd[1])

print("horizontal position: " + str(horizontal_pos))
print("depth: " + str(depth))
print("toal: " + str(horizontal_pos * depth))