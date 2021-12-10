import sys
import pathlib

def parse_input(puzzle_input: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    """Parse the puttle input"""
    input = puzzle_input.split('\n')
    

if __name__ == "__main__":
    path = sys.argv[1]
    puzzle_input = pathlib.Path(path).read_text().strip()
    
