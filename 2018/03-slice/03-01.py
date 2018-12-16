# Advent of Code 2018
# https://adventofcode.com/2018/day/3
# Dany Farina (danyluis@gmail.com)

import re
from collections import namedtuple;
from sys import *

expr   = re.compile(r"#(\d+)\s*@\s*(\d+),(\d+)\s*:\s*(\d+)x(\d+)")
fabric = [[0] * 1000 for _ in xrange(1000)]

for line in stdin.readlines():
    id, x, y, w, h = [int(s) for s in expr.split(line)[1:6]]
    for j in xrange(y, y + h):
        for i in xrange(x, x + w):
            fabric[i][j] += 1

print sum([sum([1 for j in xrange(len(fabric[i])) if fabric[i][j] > 1]) for i in xrange(len(fabric))])

