#!/usr/bin/env python

# Advent of Code 2015
# https://adventofcode.com/2015/day/1

import sys
from collections import Counter

for line in sys.stdin:
    cter = Counter(line)
    print(cter["("] - cter[")"])
