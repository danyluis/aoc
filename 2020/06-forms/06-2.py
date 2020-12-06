#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/6

import sys
from collections import Counter

group_yesses = Counter()
group_length = 0
result = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        result += sum(1 for v in group_yesses.values() if v == group_length)
        group_yesses = Counter()
        group_length = 0
    else:
        group_yesses.update(line)
        group_length += 1

result += sum(1 for v in group_yesses.values() if v == group_length)

print(f'Number of group all yesses: {result}')