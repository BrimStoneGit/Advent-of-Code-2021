# rating:
#   1 if oxygen should be calculated
#   0 if co2 should be calculated
def calculate_value(rating):
    list_of_numbers = []
    occurences = 0
    for line in open("puzzle_input.txt"):
        num = int(line, base = 2)
        list_of_numbers.append(num)

    pos = 12
    while len(list_of_numbers) > 1:
        pos -= 1
        occurences = 0
        # count occurences of 1s on position "pos"
        for num in list_of_numbers:
            if num & (1 << pos) >= 1:
                occurences += 1
        # set the number to filter by
        if rating == 1:
            filter = 1 if occurences >= (len(list_of_numbers) / 2) else 0
        else:
            filter = 0 if occurences >= (len(list_of_numbers) / 2) else 1
        # filter out every element whithout the given bit at the given position
        list_of_numbers = [x for x in list_of_numbers if bit_criteria(x, pos, filter)]
    return list_of_numbers[0]



def bit_criteria(num, pos, filter):
    bit_mask = (1 << pos)
    if num & bit_mask == 0 and filter == 0:
        return True
    elif num & bit_mask > 0 and filter == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    oxygen = calculate_value(1)
    co2 = calculate_value(0)
    print("Oxygen: " + str(oxygen))
    print("CO2: " + str(co2))
    print("Product: " + str(oxygen * co2))

