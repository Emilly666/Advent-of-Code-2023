from pathlib import Path
from heapq import heappush, heappop
from pprint import pprint

def main():
    pprint(f("input.txt"))

def f(filename = "input.txt"):
    input = initialize(filename)
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        cost, row, col, d_row, d_col, steps = heappop(pq)
        
        if row == len(input) - 1 and col == len(input[0]) - 1 and steps > 3:
            return(cost)

        if (row, col, d_row, d_col, steps) in seen:
            continue
        
        seen.add((row, col, d_row, d_col, steps))

        if steps < 10 and (d_col, d_row) != (0, 0):
            new_row = row + d_row
            new_col = col + d_col
            if 0 <= new_row < len(input) and 0 <= new_col < len(input[0]):
                heappush(pq, (cost + input[new_row][new_col], new_row, new_col, d_row, d_col, steps + 1))

        if steps > 3 or (d_row, d_col) == (0, 0):
            for new_d_row, new_d_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (new_d_row, new_d_col) != (d_row, d_col) and (new_d_row, new_d_col) != (-d_row, -d_col):
                    new_row = row + new_d_row
                    new_col = col + new_d_col
                    if 0 <= new_row < len(input) and 0 <= new_col < len(input[0]):
                        heappush(pq, (cost + input[new_row][new_col], new_row, new_col, new_d_row, new_d_col, 1))

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        grid = [list(map(int, x)) for x in file.read().split('\n')]
    return grid

if __name__ == "__main__":
    main()