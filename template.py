from pathlib import Path
from pprint import pprint

def main():
    pprint(f("test.txt"))

def f(filename = "input.txt"):
    text = initialize(filename)
    return text

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read()
    return lines

if __name__ == "__main__":
    main()