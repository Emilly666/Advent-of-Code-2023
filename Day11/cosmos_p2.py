from pathlib import Path
from pprint import pprint

def main():
    pprint(cosmic_expansion("input.txt"))

def cosmic_expansion(filename = "input.txt"):
    map = initialize(filename)
    map, empty_rows, empty_columns = expand(map)
    galaxies_pairs = find_galaxies(map)
    galaxies_distances = [distance(pair, empty_rows, empty_columns) for pair in galaxies_pairs]
    return f"Empty rows: {empty_rows}, empty columns: {empty_columns}", f"Galaxies: {sum(galaxies_distances)}"

def distance(pair, empty_rows, empty_columns):
    inc = 1000000
    sum = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
    for x in empty_rows:
        if  min(pair[0][0], pair[1][0]) < x < max(pair[0][0], pair[1][0]):
            sum += inc - 1
    for x in empty_columns:
        if  min(pair[0][1], pair[1][1]) < x < max(pair[0][1], pair[1][1]):
            sum += inc - 1
    return sum

def find_galaxies(map):
    positions = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "#":
                positions.append((x,y))
    return [(a, b) for idx, a in enumerate(positions) for b in positions[idx + 1:]]

def expand(map):
    i, j = 0, 0
    empty_rows, empty_columns = [], []
    while i < len(map):
        # expend rows
        if all([x == "." for x in map[i]]):
            empty_rows.append(i)
        # expanf collumns
        if all([map[x][j] == "." for x in range(len(map))]):
            empty_columns.append(j)
        i += 1
        j += 1
    return map, empty_rows, empty_columns

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        map = [list(x) for x in file.read().split("\n")]
        return map

if __name__ == "__main__":
    main()