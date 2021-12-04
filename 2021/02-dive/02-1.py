#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/2

import sys

xpos, depth = 0, 0

for line in sys.stdin.readlines():
    str_command, str_quant = [word.strip() for word in line.split(" ")]
    quant = int(str_quant)
    if str_command == "forward":
        xpos += quant
    elif str_command == "down":
        depth += quant
    elif str_command == "up":
        depth -= quant

print(xpos * depth)

