#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/14

import sys
from collections import Counter

lines = list(map(lambda s: s.strip(), sys.stdin.readlines()))

polymer = lines[0]
rules = {r[0] : r[1] for r in map(lambda l: tuple(l.split(' -> ')), lines[2:])}
pairs = Counter([polymer[i : i + 2] for i in range(len(polymer) - 1)])

for s in range(int(sys.argv[1])):
    new_pairs = Counter()
    for pair, cnt in pairs.items():
        if pair in rules:
            insertion = rules[pair]
            new_pairs[pair[0] + insertion] += cnt
            new_pairs[insertion + pair[1]] += cnt
        else:
            new_pairs[pair] += cnt
    pairs = new_pairs


cter = Counter([polymer[-1]])
for pair, cnt in pairs.items():
    cter[pair[0]] += cnt

print(f'character count: {cter}')
diff = max(cter.values()) - min(cter.values())
print(f'diff = {diff}')

