# Solution to Day 1 in AdventOfCode. 
# See https://adventofcode.com/

import json

with open('Day1/puzzleInput.json') as file:
    puzzleInput = json.load(file)

print('Answer to part one:', sum(puzzleInput))

# Store in a set to to increase speed of find in function
pastFrequencies = set()
currentFrequency = 0
iteration = 0

while currentFrequency not in pastFrequencies:
    pastFrequencies.add(currentFrequency)
    currentFrequency += puzzleInput[iteration % len(puzzleInput)]
    iteration += 1

print('Answer to part two:', currentFrequency)
