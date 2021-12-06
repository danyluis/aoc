#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/6

import sys

def main():
    days = int(sys.argv[1])
    fish = [0] * 9

    for d in [int(d) for d in sys.stdin.readline().strip().split(",")]:
        fish[d] += 1

    for d in range(days):
        fish = fish[1:7] + [fish[7] + fish[0], fish[8], fish[0]]

    print(sum(fish))


main()