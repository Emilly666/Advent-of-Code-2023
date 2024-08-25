from pathlib import Path
from itertools import cycle
from math import lcm

ROOT_DIR = Path(__file__).parent

def main():

    #print(navigate())
    print(navigate_ghosts())

def navigate_ghosts(filename = "input.txt"):
    instructions, nodes = initialize(filename)
    start_nodes = [node for node in nodes if node.endswith("A")]
    steps = []
    
    for node in start_nodes:
        steps.append(loop(instructions, nodes, node))

    return lcm(*steps)
    
def loop(instructions, nodes, node):
    current_node = node
    steps = 0

    for direction in cycle(instructions):
        if direction == 'L':
            current_node = nodes[current_node][0]
        elif direction == 'R':
            current_node = nodes[current_node][1]
        steps += 1

        if current_node.endswith("Z"):
            return steps

def initialize(filename):
    with open(ROOT_DIR / filename, "r") as file:
        lines = file.read().strip().replace("\n\n", "\n").splitlines()
    node_map = {}
    for line in lines[1:]:
        node, connections = line.split(' = ')
        left_node, right_node = connections.strip('()').split(', ')
        node_map[node] = (left_node, right_node)
    return lines[0], node_map

def navigate(filename = "input.txt"):
    instructions, node_map = initialize(filename)
    current_node = "AAA"
    steps = 0

    for direction in cycle(instructions):
        if direction == 'L':
            current_node = node_map[current_node][0]
        elif direction == 'R':
            current_node = node_map[current_node][1]
        steps += 1

        if current_node == 'ZZZ':
            return steps

if __name__ == "__main__":
    main()