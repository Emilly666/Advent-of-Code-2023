from pathlib import Path
from pprint import pprint

def main():
    pprint(cosmic_expansion("input.txt"))

def cosmic_expansion(filename = "input.txt"):
    map, original_size = initialize(filename)
    map, expanded_size = expand(map)
    galaxies_pairs = find_galaxies(map)
    galaxies_pairs = [distance(pair) for pair in galaxies_pairs]
    return f"Original size: {original_size}", f"Expanded size: {expanded_size}", f"Galaxies: {sum(galaxies_pairs)}"

def distance(pair):
    return abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

def find_galaxies(map):
    positions = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == "#":
                positions.append((x,y))
    return [(a, b) for idx, a in enumerate(positions) for b in positions[idx + 1:]]

def expand(map):
    i, j = 0, 0
    while i < len(map):
        # expend rows
        if all([x == "." for x in map[i]]):
            map.insert(i, ["." for x in range(len(map[i]))])
            i += 1
        # expanf collumns
        if all([map[x][j] == "." for x in range(len(map))]):
            for x in range(len(map)):
                map[x].insert(j, ".")
            j += 1
        i += 1
        j += 1
    return map, (len(map), len(map[0]))

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        map = [list(x) for x in file.read().split("\n")]
        return map, (len(map), len(map[0]))

if __name__ == "__main__":
    main()