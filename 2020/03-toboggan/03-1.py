#!/usr/bin/env python
import sys

pattern = []
for line in sys.stdin:
    line = line.strip():
    if line:
        pattern.append(line)

height = len(pattern)
width = len(pattern[0])

col, row, trees = 0, 0, 0

while row < height - 1:
    col = (col + 3) % width
    row += 1
    trees = trees + (1 if pattern[row][col] == "#" else 0)

print(f'Tree count: {trees}')
