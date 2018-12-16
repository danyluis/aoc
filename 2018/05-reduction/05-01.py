# Advent of Code 2018
# https://adventofcode.com/2018/day/5
# Dany Farina (danyluis@gmail.com)

from sys import *

def fold(a, b):
    return a.isupper() != b.isupper() and a.lower() == b.lower()

def react(line):
    while True:
        nuked = [0] * len(line)
        someNuked = False
        for i in xrange(len(line) - 1):
            if nuked[i] or nuked[i+1]:
                continue
            if fold(line[i], line[i+1]):
                nuked[i] = nuked[i+1] = 1
                someNuked = True
        if not someNuked:
            break
        line = "".join([line[i] if not nuked[i] else "" for i in xrange(len(line))])
    return line
    
for line in stdin.readlines():
    print len(react(line.strip()))