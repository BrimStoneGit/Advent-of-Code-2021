import sys
import pathlib

def parse_input(puzzle_input: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """Parse the puttle input"""
    input = puzzle_input.split('\n')
    x_transition = (0, 0)
    y_transition = (0, 0)
    result: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for line in input:
        coordinates = line.split(" -> ")
        x_transition = (int(coordinates[0].split(",")[0]), int(coordinates[1].split(",")[0]))
        y_transition = (int(coordinates[0].split(",")[1]), int(coordinates[1].split(",")[1]))
        result.append((x_transition, y_transition))
    return result

    

if __name__ == "__main__":
    path = sys.argv[1]
    puzzle_input = pathlib.Path(path).read_text().strip()
    parsed_input = parse_input(puzzle_input)
    matrix = [[0] * 1000 for _ in range(1000)]
    for transition in parsed_input:
        if transition[0][0] == transition[0][1]:
            for coord in range(min(transition[1][0], transition[1][1]), max(transition[1][0], transition[1][1]) + 1):
                matrix[transition[0][0]][coord] += 1
        elif transition[1][0] == transition[1][1]:
            for coord in range(min(transition[0][0], transition[0][1]), max(transition[0][0], transition[0][1]) + 1):
                matrix[coord][transition[1][0]] += 1
        else:
            if transition[0][0] < transition[0][1]:
                if transition[1][0] < transition[1][1]:
                    for i in range(abs(transition[0][0] - transition[0][1]) + 1):
                        matrix[transition[0][0] + i][transition[1][0] + i] += 1
                else:
                    for i in range(abs(transition[0][0] - transition[0][1]) + 1):
                        matrix[transition[0][0] + i][transition[1][0] - i] += 1
            else:
                if transition[1][0] < transition[1][1]:
                    for i in range(abs(transition[0][0] - transition[0][1]) + 1):
                        matrix[transition[0][0] - i][transition[1][0] + i] += 1
                else:
                    for i in range(abs(transition[0][0] - transition[0][1]) + 1):
                        matrix[transition[0][0] - i][transition[1][0] - i] += 1


    count = 0
    for line in matrix:
        for element in line:
            if element > 1:
                count += 1
    print(count)
