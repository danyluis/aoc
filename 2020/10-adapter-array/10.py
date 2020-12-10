#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/10

import sys
from collections import defaultdict

adapters = {int(line.strip()) for line in sys.stdin.readlines() if line.strip()}
adapters |= {0, max(adapters) + 3}

# Part 1
differences = defaultdict(int)
curr = 0
while curr < max(adapters):
    nxt = next(i for i in range(curr + 1, curr + 4) if i in adapters)
    differences[nxt - curr] += 1
    curr = nxt
print(f'diff[1] * diff[3] = {differences[1] * differences[3]}')

# Part 2
ways = {}
def count_ways(i):
    if i in ways:
        return ways[i]

    if i == 0:
        ways[i] = 1
    else:
        ways[i] = sum(count_ways(j) for j in range(i - 3, i) if j in adapters)

    return ways[i]

print(f'Number of adapter arrangements: {count_ways(max(adapters))}')


