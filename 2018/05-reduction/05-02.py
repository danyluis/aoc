# Advent of Code 2018
# https://adventofcode.com/2018/day/5
# Dany Farina (danyluis@gmail.com)

from sys import *

def fold(a, b):
    return a.isupper() != b.isupper() and a.lower() == b.lower()

def react(line):
    while True:
        nuked = [0] * len(line)
        nothingNuked = True
        for i in xrange(len(line) - 1):
            if nuked[i] or nuked[i+1]:
                continue
            if fold(line[i], line[i+1]):
                nuked[i] = nuked[i+1] = 1
                nothingNuked = False
        if nothingNuked:
            break
        line = [line[i] for i in xrange(len(line)) if not nuked[i]]
    return line
    
for line in stdin.readlines():
    line = line.strip()
    chars = set([a.lower() for a in line])

    minLen = float("inf")
    for c in chars:
        lineChars = [a for a in line if a.lower() != c] 
        minLen = min(minLen, len(react(lineChars)))
    print minLen