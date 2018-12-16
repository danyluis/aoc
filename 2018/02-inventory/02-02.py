# Advent of Code 2018
# https://adventofcode.com/2018/day/2
# Dany Farina (danyluis@gmail.com)

from sys import *
from collections import *

def diffByOne(a, b):
    if len(a) != len(b):
        return ""

    diffs = [i for i in xrange(len(a)) if a[i] != b[i]]
    if len(diffs) > 1:
        return ""

    return a[ : diffs[0]] + a[diffs[0] + 1 : ]


lines = [line.strip() for line in stdin.readlines()]
for i in xrange(len(lines) - 1):
    for j in xrange(i + 1, len(lines)):
        diff = diffByOne(lines[i], lines[j])
        if diff:
            print diff
