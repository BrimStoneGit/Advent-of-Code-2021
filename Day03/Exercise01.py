occurences = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in open("puzzle_input.txt"):
    num = int(line, base = 2)
    iterator = 0
    while num > 0:
        if (num % 2) == 1:
            occurences[iterator] += 1
        num = num >> 1
        iterator += 1
num_lines = sum(1 for line in open('puzzle_input.txt'))
gamma_rate = 0
# Bits got read from right to left, the list got written from left to right
# The gamme rate will be constructed from left to right, so the list must get reversed
occurences.reverse()
for value in occurences:
    if value > (num_lines / 2):
        gamma_rate = (gamma_rate << 1) + 1
    else:
        gamma_rate = gamma_rate << 1
# We need unsigned integers, so we are ANDing the two-complement inverse
# with a 12 Bit int to get rid of the sign
epsilon_rate = (~gamma_rate & 0xFFF)
print(epsilon_rate * gamma_rate)