from pathlib import Path
from pprint import pprint

lines = [x.split(' -> ') for x in open(Path(__file__).parent / 'input.txt', "r").read().split('\n')]

lines = [(x[0][0], x[0][1:], x[1].split(',') ) for x in lines]

def click():
    pulses = []

pprint(lines)