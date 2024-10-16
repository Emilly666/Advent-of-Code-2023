from pathlib import Path
from pprint import pprint

def main():
    pprint(f("input.txt"))

def f(filename = "input.txt"):
    instructions = initialize(filename)
    points = [(0, 0)]
    directions = { "3" : (-1, 0), "1" : (1, 0), "2" : (0, -1), "0" : (0, 1) }
    b = 0
    for line in instructions:
        n, d = line
        d_row, d_col = directions[d]
        n = int(n, 16)
        b += n
        row, col = points[-1]
        points.append((row + d_row * n, col + d_col * n))
    #shoelace formula
    A = abs(sum( points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) / 2
    #pick's theorem
    i = A - b // 2 + 1
    return i + b

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split('\n')
        rows = []
        for line in lines:
           rows.append((line.split()[2][2:7], line.split()[2][7]))
    return rows

if __name__ == "__main__":
    main()