#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/6

import sys

sum_of_yesses = 0
group_yesses = set()

for line in sys.stdin:
    line = line.strip()

    if not line:
        sum_of_yesses += len(group_yesses)
        group_yesses = set()
    else:
        group_yesses.update(line)

sum_of_yesses += len(group_yesses)

print(f'Sum of group yesses: {sum_of_yesses}')