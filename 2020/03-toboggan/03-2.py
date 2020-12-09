#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/3

import sys

pattern = [line.strip() for line in sys.stdin.readlines() if line.strip()]
height = len(pattern)
width = len(pattern[0])

answer = 1
for horiz, vert in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    col, row, trees = 0, 0, 0

    while row < height - 1:
        col = (col + horiz) % width
        row += vert
        trees = trees + (1 if pattern[row][col] == "#" else 0)

    answer *= trees

print(f'Trees multiplied: {answer}')