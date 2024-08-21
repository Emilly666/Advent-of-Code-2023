from pathlib import Path
import re
from pprint import pprint

ROOT_DIR = Path(__file__).parent

def main():
    #print(cube())
    print(cube_power())

def cube_power(filename = "input.txt"):
    # get string with input content
    text = open(ROOT_DIR / filename, "r")
    
    # create list(games) of dictionaries(game) of id's and dictionares(set)
    games = []
    for line in text: # each game
        game = {}
        match_game = re.search(r"Game (\d+): (.*)", line)
        game["id"] = int(match_game.group(1))
        game["sets"] = []
        game["red_min"] = 0
        game["green_min"] = 0
        game["blue_min"] = 0
        for set in match_game.group(2).split(";"): # each set in game
            red = re.search(r"(\d*) red", set)
            red = int(red.group(1)) if red else 0
            game["red_min"] = max(game["red_min"], red)

            green = re.search(r"(\d*) green", set)
            green = int(green.group(1)) if green else 0
            game["green_min"] = max(game["green_min"], green)

            blue = re.search(r"(\d*) blue", set)
            blue = int(blue.group(1)) if blue else 0
            game["blue_min"] = max(game["blue_min"], blue)

            game["sets"].append(
                {
                    "red" : red,
                    "green" : green,
                    "blue" : blue,
                }
            )
        game["power"] = game["red_min"] * game["green_min"] * game["blue_min"]
        games.append(game)
    #pprint(games)

    # return sum powers of all games
    return sum([ game["power"] for game in games])

def cube(filename = "input.txt", red_max = 12, green_max = 13, blue_max = 14):
    # get string with input content
    text = open(ROOT_DIR / filename, "r")
    
    # create list(games) of dictionaries(game) of id's and dictionares(set)
    games = []
    for line in text: # each game
        game = {}
        match_game = re.search(r"Game (\d+): (.*)", line)
        game["id"] = int(match_game.group(1))
        game["sets"] = []
        game["possible"] = True
        for set in match_game.group(2).split(";"): # each set in game
            red = re.search(r"(\d*) red", set)
            red = int(red.group(1)) if red else 0

            green = re.search(r"(\d*) green", set)
            green = int(green.group(1)) if green else 0

            blue = re.search(r"(\d*) blue", set)
            blue = int(blue.group(1)) if blue else 0

            game["sets"].append(
                {
                    "red" : red,
                    "green" : green,
                    "blue" : blue,
                }
            )
            game["possible"] = red <= red_max and green <= green_max and blue <= blue_max and game["possible"]
        games.append(game)
    #pprint(games)

    # return sum of id's of all possible games
    return sum([ game["id"] for game in games if game["possible"]])

if __name__ == "__main__":
    main()