# Advent of Code 2018
# https://adventofcode.com/2018/day/3
# Dany Farina (danyluis@gmail.com)

from collections import *;
from sys import *
from re import *

DIM    = 1000
fabric = [[[] for x in range(DIM)] for y in range(DIM)]
lines  = stdin.readlines()
claims = list()

#1 @ 12,548: 19x10
reClaim = compile(r"^#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)$")

for line in lines:
    id, x, y, w, h = [int(i) for i in reClaim.split(line.strip()) if len(i)]
    for j in xrange(y, y + h):
        for i in xrange(x, x + w):
            fabric[i][j].append(id)
    claims.append((id, x, y, w, h))

for (id, x, y, w, h) in claims:
    if any(any(len(fabric[i][j]) > 1 for i in xrange(x, x + w)) for j in xrange(y, y + h)):
        continue
    print id
    break
