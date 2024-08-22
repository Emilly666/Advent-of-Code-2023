from pathlib import Path
from pprint import pprint
import gc

ROOT_DIR = Path(__file__).parent

def main():
    #print(seed())
    print(seed_with_ranges2("input.txt"))
    

def seed_with_ranges2(filename="input.txt"):
    text = open(ROOT_DIR / filename, "r").read().splitlines()

    # Find the start indices of each map
    starts = [i for i, line in enumerate(text) if not line]

    # Create list of maps with corrected variable name
    map_sections = [
        [list(map(int, text[idx].split())) for idx in range(value + 2, starts[i + 1])]
        for i, value in enumerate(starts[:-1])
    ]

    minseed = float('inf')

    # Extract seed ranges
    seed_ranges = list(map(int, text[0].split()[1:]))

    # Process each seed range
    for i in range(0, len(seed_ranges), 2):
        start, length = seed_ranges[i], seed_ranges[i + 1]
        print(f"current seed range start: {start}, length: {length}")

        for seed in range(start, start + length):
            original_seed = seed
            for section in map_sections:  # Rename map to section
                for row in section:
                    start_range, length_range, delta = row[1], row[2], row[0]
                    if start_range <= seed < start_range + length_range:
                        seed += delta - start_range
                        break  # Stop checking this map since a change was made

            minseed = min(minseed, seed)

    return minseed

def seed_with_ranges(filename="input.txt"):
    text = open(ROOT_DIR / filename, "r").read().splitlines()
    
    # Find the start indices of each map
    starts = [i for i, line in enumerate(text) if not line]
    
    maps = [
        [text[idx] for idx in range(value + 2, starts[i + 1])]
        for i, value in enumerate(starts[:-1])
    ]

    minseed = float('inf')

    # Extract seed ranges
    seed_starts = list(map(int, text[0].split()[1:]))
    
    # Process each seed range
    for i in range(0, len(seed_starts), 2):
        start, count = seed_starts[i], seed_starts[i + 1]
        print(f"current seed range start: {i}")
        
        for seed in range(start, start + count):
            original_seed = seed
            
            # Apply each map to the seed
            for map in maps:
                for r in map:
                    row = list(map(int, r.split()))
                    if row[1] <= seed < row[1] + row[2]:
                        seed += (row[0] - row[1])
                        break  # No need to check further in this map
            
            minseed = min(minseed, seed)
            seed = original_seed  # Reset seed for next iteration

    return minseed

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