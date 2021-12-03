count = 0
acc = -1
with open("puzzle_input.txt") as input: 
    acc = int(input.readline())
    for line in input:
        if int(line) > acc:
            count += 1
        acc = int(line)
        
print(count)