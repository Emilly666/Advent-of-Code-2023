from pathlib import Path
from pprint import pprint

def main():
    pprint(pipes_area("test.txt"))

def pipes_area(filename = "input.txt"):
    text = initialize(filename)
    map = [[*line] for line in text]
    steps = 0
    directions = {
        "down"  : { "|" : "down",  "L" : "right", "J" : "left", "S": "down" },
        "left"  : { "-" : "left",  "L" : "up",    "F" : "down"  },
        "up"    : { "|" : "up",    "7" : "left",  "F" : "right" },
        "right" : { "-" : "right", "J" : "up",    "7" : "down"  }
    }    
    position = find_S(map)
    go_next = "down"

    while map[position[0]][position[1]] in ["|", "-", "L", "J", "7", "F", "S"]:
        
        map[position[0]][position[1]] = '#'
        match go_next:
            case "down":
                position[0] += 1
            case "left":
                position[1] -= 1
            case "up":
                position[0] -= 1
            case "right":
                position[1] += 1
        steps +=1
        if map[position[0]][position[1]] == '#':
            return map
        go_next = directions[go_next][map[position[0]][position[1]]]

def pipes(filename = "input.txt"):
    text = initialize(filename)
    map = [[*line] for line in text]
    steps = 0
    directions = {
        "down"  : { "|" : "down",  "L" : "right", "J" : "left", "S": "down" },
        "left"  : { "-" : "left",  "L" : "up",    "F" : "down"  },
        "up"    : { "|" : "up",    "7" : "left",  "F" : "right" },
        "right" : { "-" : "right", "J" : "up",    "7" : "down"  }
    }    
    position = find_S(map)
    go_next = "down"

    while map[position[0]][position[1]] in ["|", "-", "L", "J", "7", "F", "S"]:
        
        map[position[0]][position[1]] = steps
        match go_next:
            case "down":
                position[0] += 1
            case "left":
                position[1] -= 1
            case "up":
                position[0] -= 1
            case "right":
                position[1] += 1
        steps +=1
        if map[position[0]][position[1]] == 0:
            return steps // 2
        go_next = directions[go_next][map[position[0]][position[1]]]

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split("\n")
    return lines

def find_S(map):
    for i, row in enumerate(map):
        for j, element in enumerate(row):
            if element == 'S':
                return [i, j]
    return None

if __name__ == "__main__":
    main()