from pathlib import Path
from pprint import pprint

def main():
    pprint(f("input.txt"))

def f(filename = "input.txt"):
    grid = initialize(filename)
    xmax, ymax = len(grid[0])-1, len(grid)-1
    max = 0
    for x in range(xmax):
        count = energize([(x, 0, 'right')], grid, xmax, ymax)
        if count > max:
            max = count
        count = energize([(x, xmax, 'left')], grid, xmax, ymax)
        if count > max:
            max = count
    for y in range(ymax):
        count = energize([(0, y, 'down')], grid, xmax, ymax)
        if count > max:
            max = count
        count = energize([(ymax, y, 'up')], grid, xmax, ymax)
        if count > max:
            max = count
    return max
    
    

def energize(check, grid, xmax, ymax):
    energized = set()
    while(len(check) > 0):
        check_now = check.pop(0)
        char = grid[check_now[0]][check_now[1]]
        
        if check_now not in energized:
            energized.add(check_now)
            match char:
                case '.':
                    match check_now[2]:
                        case 'right':
                            if check_now[1] + 1 <= xmax:
                                check.append((check_now[0], check_now[1] + 1, 'right'))
                        case 'left':
                            if check_now[1] -1 >= 0:
                                check.append((check_now[0], check_now[1] - 1, 'left'))
                        case 'down':
                            if check_now[0] + 1 <= ymax:
                                check.append((check_now[0] + 1, check_now[1], 'down'))
                        case 'up':
                            if check_now[0] - 1 >= 0:
                                check.append((check_now[0] - 1, check_now[1], 'up'))
                case '|':
                    match check_now[2]:
                        case 'right' | 'left':
                            if check_now[0] + 1 <= ymax:
                                check.append((check_now[0] + 1, check_now[1], 'down'))
                            if check_now[0] - 1 >= 0:
                                check.append((check_now[0] - 1, check_now[1], 'up'))
                        case 'down':
                            if check_now[0] + 1 <= ymax:
                                check.append((check_now[0] + 1, check_now[1], 'down'))
                        case 'up':
                            if check_now[0] - 1 >= 0:
                                check.append((check_now[0] - 1, check_now[1], 'up'))
                case '-':
                    match check_now[2]:
                        case 'right':
                            if check_now[1] + 1 <= xmax:
                                check.append((check_now[0], check_now[1] + 1, 'right'))
                        case 'left':
                            if check_now[1] -1 >= 0:
                                check.append((check_now[0], check_now[1] - 1, 'left'))
                        case 'down' | 'up':
                            if check_now[1] + 1 <= xmax:
                                check.append((check_now[0], check_now[1] + 1, 'right'))
                            if check_now[1] -1 >= 0:
                                check.append((check_now[0], check_now[1] - 1, 'left'))
                case '/':
                    match check_now[2]:
                        case 'right':
                            if check_now[0] - 1 >= 0:
                                check.append((check_now[0] - 1, check_now[1], 'up'))
                        case 'left':
                            if check_now[0] + 1 <= ymax:
                                check.append((check_now[0] + 1, check_now[1], 'down'))
                        case 'down':
                            if check_now[1] -1 >= 0:
                                check.append((check_now[0], check_now[1] - 1, 'left'))
                        case 'up':
                            if check_now[1] + 1 <= xmax:
                                check.append((check_now[0], check_now[1] + 1, 'right'))
                case '\\':
                    match check_now[2]:
                        case 'right':
                            if check_now[0] + 1 <= ymax:
                                check.append((check_now[0] + 1, check_now[1], 'down'))
                        case 'left':
                            if check_now[0] - 1 >= 0:
                                check.append((check_now[0] - 1, check_now[1], 'up'))
                        case 'down':
                            if check_now[1] + 1 <= xmax:
                                check.append((check_now[0], check_now[1] + 1, 'right'))
                        case 'up':
                            if check_now[1] -1 >= 0:
                                check.append((check_now[0], check_now[1] - 1, 'left'))
    energized2 = set()
    for x in energized:
        energized2.add((x[0], x[1]))
    return len(energized2)

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        grid = [[*x] for x in file.read().split('\n')]
    return grid

if __name__ == "__main__":
    main()