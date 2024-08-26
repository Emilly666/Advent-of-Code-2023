from pathlib import Path
from pprint import pprint

def main():
    pprint(f("test.txt"))

def f(filename = "input.txt"):
    text = initialize(filename)
    map = [[*line] for line in text]
    start_index = find_S(map)
    return start_index, map[start_index[0]][start_index[1]]

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read()
    return lines

def find_S(map):
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == 'S':
                return (i, j)
    return None

if __name__ == "__main__":
    main()