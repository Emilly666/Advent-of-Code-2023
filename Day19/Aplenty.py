from pathlib import Path
from pprint import pprint
import re

def main():
    pprint(f("test.txt"))

def f(filename = "input.txt"):
    workflows, parts = initialize(filename)
    total = 0

    for part in parts:
        if accept(workflows, part):
            total += sum([x for x in part])
    return total


operators = {
    ">" : int.__gt__,
    "<" : int.__lt__
}
def accept(workflows, part, name = "in"):
    if name == 'A':
        return True
    if name == 'R':
        return False
    conditions, default = workflows[name]

    for i, comp, n, target in conditions:
        if operators[comp](part[i], n):
            return accept(workflows, part, target)
    return accept(workflows, part, default)

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        workflows, parts = file.read().split("\n\n")
        workflows, parts = workflows.split("\n"), parts.split("\n")
        parts2 = []
        workflows2 = {}
        for part in parts:
            match = re.search(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", part[1:-1])
            parts2.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))
        
        for workflow in workflows:
            name, conditions = workflow.split("{")
            conditions = conditions[:-1].split(",")
            conditions, final = conditions[:-1], conditions[-1]
            conditions2 = []
            for condition in conditions:
                match = re.search(r"([xmas])([><])(\d+):(\S+)", condition)
                conditions2.append((int(match.group(1).replace('x', '0').replace('m', '1').replace('a', '2').replace('s', '3')), match.group(2), int(match.group(3)), match.group(4)))
            workflows2[name] = (conditions2, final)
    return workflows2, parts2

if __name__ == "__main__":
    main()