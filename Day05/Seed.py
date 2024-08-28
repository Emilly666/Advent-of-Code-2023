from pathlib import Path
ROOT_DIR = Path(__file__).parent

def main():
    #print(seed())
    print(seed_with_ranges())
    
# https://youtu.be/NmxHw_bHhGM
def seed_with_ranges(filename = "input.txt"):
    inputs, *blocks = open(ROOT_DIR / filename, "r").read().split("\n\n")
    inputs = list(map(int, inputs.split(":")[1].split()))
    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []

        while seeds:
            start, end = seeds.pop()
            for a, b, c in ranges:
                overlap_start = max(start, b)
                overlap_end = min(end, b + c)
                if overlap_start < overlap_end:
                    new.append((overlap_start - b + a, overlap_end - b + a))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
        seeds = new
    return min(seeds)[0]

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