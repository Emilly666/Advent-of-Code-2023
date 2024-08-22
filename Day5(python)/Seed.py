from pathlib import Path
from pprint import pprint

ROOT_DIR = Path(__file__).parent

def main():
    print(seed())

def seed(filename = "input.txt"):
    text = open(ROOT_DIR / filename, "r").read().split("\n")
    text.append("")
    seeds = [eval(i) for i in text[0].split()[1:]]
    starts = [ i for i in range(1, len(text) ) if text[i] == '' ]
    maps = []
    
    for i, value in enumerate(starts[:-1]):
        map = []
        for idx in range(value + 2, starts[i + 1]):
            map.append(text[idx])
        maps.append(map)    
    # transalate all seeds
    for i in range(len(seeds)):
        # translate each map
        for map in maps:
            changed = False
            # check all ranges
            for r in map:
                row = r.split()
                if  int(row[1]) <= seeds[i] < int(row[1]) + int(row[2]) and not changed:
                    seeds[i] += ( int(row[0]) - int(row[1]) )
                    changed = True
    return min(seeds)

if __name__ == "__main__":
    main()