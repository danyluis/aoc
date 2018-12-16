# Advent of Code 2018
# https://adventofcode.com/2018/day/2
# Dany Farina (danyluis@gmail.com)

from sys import *
from collections import *

threes, twos = 0, 0

for line in stdin.readlines():
    line    = line.strip()
    lcter   = Counter(line)
    twos   += 1 if 2 in lcter.values() else 0
    threes += 1 if 3 in lcter.values() else 0

print twos * threes
    
