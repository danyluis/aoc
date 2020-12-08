#!/usr/bin/env python

# Advent of Code 2015
# https://adventofcode.com/2015/day/1

import sys

floor = 0
for line in sys.stdin:
    for i in range(len(line)):
        floor += 1 if line[i] == "(" else -1
        if floor == -1:
            print(i + 1)
            break
