from pathlib import Path
import re

def main():
    print(f("input.txt"))
    
def f(filename = "input.txt"):
    text = initialize(filename)
    boxes = [[] for x in range(0, 256)]
    for x in text:
        reg = re.search(r'(.+)([-=])(\d)?', x)
        box = boxes[hash(reg.group(1))]
        if reg.group(2) == '=':
            found = False
            for i, item in enumerate(box):
                if item[0] == reg.group(1):
                    box[i] = (reg.group(1), reg.group(3))
                    found = True
                    break
            if not found:
                box.append((reg.group(1), reg.group(3)))
        elif reg.group(2) == '-':
            for i, lens in enumerate(box):
                if lens[0] == reg.group(1):
                    del box[i]
                    break
    return sum((i + 1) * (y + 1) * int(lens[1]) for i, box in enumerate(boxes) for y, lens in enumerate(box))

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split(',')
    return lines

def hash(string):
    val = 0 
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val

if __name__ == "__main__":
    main()