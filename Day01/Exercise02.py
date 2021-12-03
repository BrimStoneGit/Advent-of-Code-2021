count = 0
upper_bound = 3
values =[]
acc1 = 0
acc2 = 0
with open("puzzle_input.txt") as input: 
    values = input.readlines()
    values = [int(i) for i in values]

acc1 = sum(values[upper_bound - 3:upper_bound])
upper_bound += 1
while upper_bound <= len(values):
    acc2 = sum(values[upper_bound - 3:upper_bound])
    print(str(acc2) + " is bigger than " + str(acc1))
    if acc2 > acc1:
        count += 1
        print("yes")
    acc1 = acc2
    upper_bound += 1

print("Upper bound: " + str(upper_bound))        
print(count)