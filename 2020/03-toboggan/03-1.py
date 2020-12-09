#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/3

import sys

pattern = [line.strip() for line in sys.stdin.readlines() if line.strip()]
height = len(pattern)
width = len(pattern[0])

col, row, trees = 0, 0, 0

while row < height - 1:
    col = (col + 3) % width
    row += 1
    trees = trees + (1 if pattern[row][col] == "#" else 0)

print(f'Tree count: {trees}')
