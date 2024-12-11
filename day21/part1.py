from pathlib import Path
from collections import deque

directions = [(-1, 0), (1, 0), [0, -1], (0, 1)]
file = open(Path(__file__).parent / 'test.txt', "r").read().split('\n')
start = [(ix,iy) for ix, row in enumerate(file) for iy, i in enumerate(row) if i == 'S'][0]

possible = deque(start)

for _ in range(64):
    for position in possible:
        
        for d in directions:
            if file[position[0] + d[0]][position[1] + d[1]] != '#':
                possible.append((position[0] + d[0], position[1] + d[1]))

    

print(len(possible))