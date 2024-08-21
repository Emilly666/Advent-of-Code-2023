from pathlib import Path

ROOT_DIR = Path(__file__).parent

def main():
    file = open(ROOT_DIR / "input.txt", "r")

    for line in file:
        print(line, end="")


if __name__ == "__main__":
    main()