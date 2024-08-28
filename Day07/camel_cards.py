from pathlib import Path

ROOT_DIR = Path(__file__).parent

def main():
    print(cards())

def cards(filename = "input.txt"):
    input = [[[*x.split()[0]], x.split()[1]] for x in open(ROOT_DIR / filename, "r").read().split("\n")]
    hands = []
    # prepare input
    for hand in input:
        x = [int(x.replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13").replace("A", "14")) for x in hand[0]]
        hands.append({
            "cards" : x,
            "bid" : int(hand[1]),
            "type" : check_type(x)
        })
    hands = sorted(hands, key = lambda x : str(x["type"]) + str(x["cards"][0]).zfill(2) + str(x["cards"][1]).zfill(2) + str(x["cards"][2]).zfill(2) + str(x["cards"][3]).zfill(2) + str(x["cards"][4]).zfill(2))

    return sum([ hand["bid"] * (i + 1) for i, hand in enumerate(hands) ])

def check_type(cards):
    appearances = sorted([ 
        cards.count(2), cards.count(3), cards.count(4), 
        cards.count(5), cards.count(6), cards.count(7), 
        cards.count(8), cards.count(9), cards.count(10), 
        cards.count(11), cards.count(12), cards.count(13), cards.count(14)])[::-1]
    # 5, 4 of a kind
    if appearances[0] in [4,5]:
        return appearances[0] + 1
    # full house
    elif appearances[0] == 3 and appearances[1] == 2:
        return 4
    # 3 of a kind
    elif appearances[0] == 3 and appearances[1] != 2:
        return 3
    # two pairs
    elif appearances[0] == 2 and appearances[1] == 2:
        return 2
    # pair
    elif appearances[0] == 2 and appearances[1] != 2:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()