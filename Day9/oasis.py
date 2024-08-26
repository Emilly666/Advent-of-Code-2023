from pathlib import Path
from pprint import pprint

def main():
    #pprint(mirage("test.txt"))
    pprint(mirage("input.txt", False))

def mirage(filename = "input.txt", forward = True):
    readings = initialize(filename)
    data = []
    for reading in readings:
        rows = [reading]
        
        while not all([x == 0 for x in rows[-1]]):
            row = []
            for i in range(len(rows[-1][:-1])):
                row.append(rows[-1][i + 1] - rows[-1][i])
            rows.append(row)
        else:
            rows[-1].append(0)

        if forward: # extrapolate
            for i in range(len(rows)-2, -1, -1):
                rows[i].append(rows[i][-1] + rows[i + 1][-1])
        else:
            for i in range(len(rows)-2, -1, -1):
                rows[i].insert(0, rows[i][0] - rows[i + 1][0])
        data.append(rows)

    if forward:
        return sum([x[0][-1] for x in data ])
    else:
        return sum([x[0][0] for x in data ])
    
    
def initialize(filename):
    with open(Path(__file__).parent / filename, "r") as file:
        lines = file.read().split("\n")
    histories = []
    for line in lines:
        histories.append([eval(x) for x in line.split()])
    return histories

if __name__ == "__main__":
    main()