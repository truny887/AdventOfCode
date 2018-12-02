# Solution to Day 2 in AdventOfCode. 
# See https://adventofcode.com/

import json
from collections import Counter

with open('Day2/puzzleInput.json') as file:
    puzzleInput = json.load(file)

with open('Day2/exampleInput.json') as file:
    exampleInput = json.load(file)

def checksumCalculator(input):
    duplicates = 0
    triplicates = 0
    for item in input:
        countedList = Counter(item)
        if 2 in countedList.values():
            duplicates += 1

        if 3 in countedList.values():
            triplicates += 1

    return duplicates*triplicates

assert checksumCalculator(exampleInput) == 12

checksumCalculator(puzzleInput)