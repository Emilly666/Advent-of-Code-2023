from functools import cache
from pathlib import Path
#https://www.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/
@cache
def recurse(lava, springs, result=0):
    if not springs:
        return '#' not in lava
    current, springs = springs[0], springs[1:]
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        if "#" in lava[:i]:
            break
        if (nxt := i + current) <= len(lava) and '.' not in lava[i : nxt] and lava[nxt : nxt + 1] != "#":
            result += recurse(lava[nxt + 1:], springs)
    return result


with open(Path(__file__).parent / "input.txt", "r") as file:
    data = [x.split() for x in file.read().splitlines()]
    p1, p2 = 0, 0
    for e, (lava, springs) in enumerate(data):
        p1 += recurse(lava, (springs := tuple(map(int, springs.split(",")))))
        p2 += recurse("?".join([lava] * 5), springs * 5)
    print(p1, p2)