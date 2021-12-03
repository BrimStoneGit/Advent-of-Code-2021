horizontal_pos = 0
depth = 0
for line in open("puzzle_input.txt"):
    cmd = line
    splitted_cmd = cmd.split(' ')
    if splitted_cmd[0] == 'forward':
        horizontal_pos += int(splitted_cmd[1])
    elif splitted_cmd[0] == 'down':
        depth += int(splitted_cmd[1])
    elif splitted_cmd[0] == 'up':
        depth -= int(splitted_cmd[1])

print("horizontal position: " + str(horizontal_pos))
print("depth: " + str(depth))
print("toal: " + str(horizontal_pos * depth))