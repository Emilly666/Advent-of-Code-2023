from pathlib import Path
import re

ROOT_DIR = Path(__file__).parent

def main():
    print(calibrate())
    print(calibrate_with_strings("input.txt"))

def calibrate_with_strings(filename = "input.txt"):
    #get string with input content
    text = open(ROOT_DIR / filename, "r")

    #create list of list of digits in every line of input
    digit_list = []
    for line in text:
        match = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        if match:
            digit_list.append(int((match[0] + match[-1])
                                  .replace("one", "1")
                                  .replace("two", "2")
                                  .replace("three", "3")
                                  .replace("four", "4")
                                  .replace("five", "5")
                                  .replace("six", "6")
                                  .replace("seven", "7")
                                  .replace("eight", "8")
                                  .replace("nine", "9")))

    #return sum of all numbers
    return sum(digit_list)

def calibrate(filename = "input.txt"):
    #get string with input content
    text = open(ROOT_DIR / filename, "r")

    #create list of list of digits in every line of input
    digit_list = []
    for line in text:
        match = re.findall(r"[0-9]", line)
        if match:
            digit_list.append(int(match[0] + match[-1]))

    #return sum of all numbers
    return sum(digit_list)

if __name__ == "__main__":
    main()