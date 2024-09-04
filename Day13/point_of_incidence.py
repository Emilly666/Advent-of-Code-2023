from pathlib import Path
from pprint import pprint

def main():
    f("test.txt")

def f(filename = "input.txt"):
    text = [Pattern(x.split("\n")) for x in initialize(filename)]
    pprint (str(text[0]))
    return text

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split("\n\n")
    return lines

class Pattern:
    def __init__(self, list_of_strings):
        self.horizontal = list_of_strings
        self.vertical = []
        for i in range(len(list_of_strings[0])):
            self.vertical.append("")
            for line in list_of_strings:
                self.vertical += line[i]
    def __str__(self):
        return f"{self.horizontal}"


if __name__ == "__main__":
    main()