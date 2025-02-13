from pathlib import Path

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
file = open(Path(__file__).parent / 'input.txt', "r").read().split('\n')
start = [(ix,iy) for ix, row in enumerate(file) for iy, i in enumerate(row) if i == 'S'][0]
cols = len(file[0])
rows = len(file)

possible = {start}

for _ in range(64):
    t = set()
    for pos in possible:
        for d in directions:
            if cols >= pos[0] + d[0] >= 0 and rows >= pos[1] + d[1] >= 0 and file[pos[0] + d[0]][pos[1] + d[1]] != '#':
                t.add((pos[0] + d[0], pos[1] + d[1]))
    possible = t

print(len(possible))