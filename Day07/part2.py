# https://www.reddit.com/r/adventofcode/comments/18cnzbm/2023_day_7_solutions/
import collections
from pathlib import Path

ROOT_DIR = Path(__file__).parent

lines = [i for i in open(ROOT_DIR /'input.txt').read().split('\n') if i.strip()]
def hand(h,part1):
    if part1: h = h.replace('J', 'X')
    h2 = ['J23456789TXQKA'.index(i)for i in h]
    ts = []
    for r in '23456789TQKA':
        c = collections.Counter(h.replace('J', r))
        p = tuple(sorted(c.values()))
        t = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(p)
        ts.append(t)
    return (max(ts), *h2)
for part1 in (True, False):
    h = sorted((hand(h,part1), int(b)) for h, b in (l.split() for l in lines))
    t = 0
    for i,(_,b) in enumerate(h):
        t+=i*b+b
    print('Part', 2-part1, ':', t)