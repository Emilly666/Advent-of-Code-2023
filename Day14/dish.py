from pathlib import Path
from pprint import pprint

def main():
    #pprint(f())
    pprint(f2())

def f(filename = "input.txt"):
    input = initialize(filename)
    output = slide_north(input)
    return sum([output[x].count("O") * (len(output) - x) for x in range(len(output))])

def f2(filename = "input.txt"):
    input = initialize(filename)
    loops = 1000000000
    seen, i = cycle(input, loops)
    output = seen[(loops - i) % (len(seen) - i) + i - 1]
    return sum([output[x].count("O") * (len(output) - x) for x in range(len(output))])

def cycle(input, x):
    seen = []
    for i in range(x):
        input = slide_north(input)
        input = slide_west(input)
        input = slide_south(input)
        input = slide_east(input)
        a = input.copy()
        if a in seen:
            return seen, seen.index(a)
        seen.append(a)
    return seen, x

def slide_north(input):
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == "O":
                slide = 1
                while i - slide >= 0 and input[i - slide][j] == ".":
                    input[i - slide] = input[i - slide][:j] + "O" + input[i - slide][j + 1:]
                    input[i - slide + 1] = input[i - slide + 1][:j] + "." + input[i - slide + 1][j + 1:]
                    slide += 1
    return input

def slide_west(input):
    for i in range(0, len(input) ):
        for j in range(0, len(input[i])):
            if input[i][j] == "O":
                slide = 1
                while j - slide >= 0 and input[i][j - slide] == ".":
                    input[i] = input[i][:j - slide] + "O." + input[i][j - slide + 2:]
                    slide += 1
    return input

def slide_south(input):
    for i in range(len(input) - 1, -1, -1):
        for j in range(0, len(input[0])):
            if input[i][j] == "O":
                slide = 1
                while i + slide < len(input)  and input[i + slide][j] == ".":
                    input[i + slide] = input[i + slide][:j] + "O" + input[i + slide][j + 1:]
                    input[i + slide - 1] = input[i + slide - 1][:j] + "." + input[i + slide - 1][j + 1:]
                    slide += 1
    return input

def slide_east(input):
    for i in range(0, len(input) ):
        for j in range( len(input[i]) - 1, -1, -1):
            if input[i][j] == "O":
                slide = 1
                while j + slide < len(input[i]) and input[i][j + slide] == ".":
                    input[i] = input[i][:j + slide - 1] + ".O" + input[i][j + slide + 1:]
                    slide += 1
    return input

def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split("\n")
    return lines

if __name__ == "__main__":
    main()