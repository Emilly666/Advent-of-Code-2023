from pathlib import Path
import math

ROOT_DIR = Path(__file__).parent

def main():
    print(boat_races2("input.txt"))

def boat_races(filename = "input.txt"):
    times = list(map(int, open(ROOT_DIR / filename, "r").read().split("\n")[0].split()[1:]))
    distances = list(map(int, open(ROOT_DIR / filename, "r").read().split("\n")[1].split()[1:]))
    races = []
    for i in range(len(times)):
        races.append({"time" : times[i], "distance" : distances[i], "hold_min" : 1, "hold_max" : times[i]})
    
    # check minimal hold times
    for race in races:
        for hold_time in range(race["hold_min"], race["hold_max"]):
            if race["distance"] < (race["time"] - hold_time) * hold_time:
                race["hold_min"] = hold_time
                break
    # check maximal hold times
    for race in races:
        for hold_time in range(race["hold_max"], race["hold_min"], -1):
            if race["distance"] < (race["time"] - hold_time) * hold_time:
                race["hold_max"] = hold_time
                race["possible_wins"] = race["hold_max"] - race["hold_min"] + 1
                break
    return math.prod([ race["possible_wins"] for race in races])

def boat_races2(filename = "input.txt"):
    time = int("".join(open(ROOT_DIR / filename, "r").read().split("\n")[0].split()[1:]))
    distance = int("".join(open(ROOT_DIR / filename, "r").read().split("\n")[1].split()[1:]))

    race = {"time" : time, "distance" : distance, "hold_min" : 1, "hold_max" : time}

    # check minimal hold times
    for hold_time in range(race["hold_min"], race["hold_max"]):
        if race["distance"] < (race["time"] - hold_time) * hold_time:
            race["hold_min"] = hold_time
            break

    # check maximal hold times
    for hold_time in range(race["hold_max"], race["hold_min"], -1):
        if race["distance"] < (race["time"] - hold_time) * hold_time:
            race["hold_max"] = hold_time
            race["possible_wins"] = race["hold_max"] - race["hold_min"] + 1
            break
    return race["possible_wins"]

if __name__ == "__main__":
    main()