from pathlib import Path
from pprint import pprint

def main():
    pprint(f("input.txt"))

def f(filename = "input.txt"):
    patterns = [Pattern(x.split("\n")) for x in initialize(filename)]
    lefts = []
    ups = []
    for patern in patterns:
        split = patern.find_horizontal()
        if split != None:
            ups.append(split)
        else:
            split = patern.find_vertical()
            lefts.append(split)
        
    return sum(lefts) + 100 * sum(ups)

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split("\n\n")
    return lines

def compare_strings(seq1, seq2):
    return sum(1 for a, b in zip(seq1, seq2) if a != b) == 1

class Pattern:
    def __init__(self, list_of_strings):
        self.horizontal = list_of_strings
        self.vertical = []
        for i in range(len(list_of_strings[0])):
            vertical_line = ''
            for line in list_of_strings:
                vertical_line += line[i]
            self.vertical.append(vertical_line)

    def find_horizontal(self):
        max = len(self.horizontal) - 1
        for i in range(0, max):
            smudge = False
            up, down = i, i + 1
            while(up >= 0 and down <= max):
                if self.horizontal[up] == self.horizontal[down]:
                    up -= 1
                    down += 1
                elif compare_strings(self.horizontal[up], self.horizontal[down]) and smudge == False:
                    smudge = True
                    up -= 1
                    down += 1
                else:
                    break
            else:
                if smudge:
                    return i + 1 
    def find_vertical(self):
        max = len(self.vertical) - 1
        for i in range(0, max):
            smudge = False
            l, r = i, i + 1
            while(l >= 0 and r <= max):
                if self.vertical[l] == self.vertical[r]:
                    l -= 1
                    r += 1
                elif compare_strings(self.vertical[l], self.vertical[r]) and smudge == False:
                    smudge = True
                    l -= 1
                    r += 1
                else:
                    break
            else:
                if smudge:
                    return i + 1

            
if __name__ == "__main__":
    main()