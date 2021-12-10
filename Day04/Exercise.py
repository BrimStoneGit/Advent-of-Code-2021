import sys
import pathlib
from typing import Any, TypeVar

def get_winning_count_per_row(row: list[int], numbers: list[int]) -> int:
    """ Calculate the amount of numbers until the row is completed """
    counter = 0
    for num in numbers:
        if num in row:
            counter += 1
            if counter == 5:
                return numbers.index(num)
    return len(numbers)

def numbers_until_winning(board: list[list[int]], numbers: list[int]) -> int:
    inverted_board = invert_board(board)
    horizontal_winning = min([get_winning_count_per_row(x, numbers) for x in board])
    vertical_winning = min([get_winning_count_per_row(x, numbers) for x in inverted_board])
    return min(horizontal_winning, vertical_winning)

def calculate_score(board: list[list[int]], number_subset: list[int], last_called: int) -> int:
    """ Calculate the score of a board on a given subset to numbers """
    return sum([x for row in board for x in row if (x not in number_subset)]) * last_called

def invert_board(board: list[list[int]]) -> list[list[int]]:
    """ Invert given board """
    inverted_board: list[list[int]] = [[], [], [], [], []]
    for row in board:
        for i in range(5):
            inverted_board[i].append(row[i])
    return inverted_board

def parse_boards(boards: list[str]) -> list[list[list[int]]]:
    """ Parsing of all boards  """
    parsed_boards: list[list[list[int]]] = []
    acc_board: list[list[int]] = []
    for row in boards:
        if len(row) > 1:
            parsed_row = [int(x) for x in row.replace("  ", " ").split(" ")]
            acc_board.append(parsed_row)
        else:
            parsed_boards.append(acc_board)
            acc_board = []
    if len(acc_board) > 0:
        parsed_boards.append(acc_board)
    return parsed_boards

def parse(input: str) -> tuple[list[int], str]:
    """ Parsing of the input string """
    input = input.split("\n")
    numbers = [int(x) for x in input[0].split(',')]
    preprocessed_data = [x.strip().replace("  ", " ") for x in input[2:]]
    boards = parse_boards(preprocessed_data)
    return (numbers, boards)

def part_1(boards: list[list[list[int]]], numbers: list[int]) -> int:
    winning_counts = [numbers_until_winning(x, numbers) for x in boards]
    score_of_winning_board = calculate_score(boards[winning_counts.index(min(winning_counts))], numbers[0:(min(winning_counts) + 1)], numbers[min(winning_counts)])
    return score_of_winning_board

def part_2(boards: list[list[list[int]]], numbers: list[int]) -> int:
    winning_counts = [numbers_until_winning(x, numbers) for x in boards]
    score_of_losing_board = calculate_score(boards[winning_counts.index(max(winning_counts))], numbers[0:(max(winning_counts) + 1)], numbers[max(winning_counts)])
    return score_of_losing_board


if __name__ == "__main__":
    path = sys.argv[1]
    puzzle_input = pathlib.Path(path).read_text().strip()
    num, boards = parse(puzzle_input)
    print(part_1(boards, num))
    print(part_2(boards, num))
