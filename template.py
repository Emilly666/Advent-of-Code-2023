from pathlib import Path

ROOT_DIR = Path(__file__).parent

def main():
    f()

def f(filename = "input.txt"):
    text = open(ROOT_DIR / filename, "r").read()
    return None

if __name__ == "__main__":
    main()