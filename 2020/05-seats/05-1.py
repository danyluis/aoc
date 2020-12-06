#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/5

import sys

def seat_code(strcode):
    return int("".join(["1" if c in ("B", "R") else "0" for c in strcode]), 2)

max_code = max(seat_code(l.strip()) for l in sys.stdin.readlines())
print(f'Maximum code is {max_code}')

