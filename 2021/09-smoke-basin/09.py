#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/9

import sys
from functools import reduce

moves = ((0, -1), (0, 1), (-1, 0), (1, 0))

def get_neighbours(heights, row, col):
    for drow, dcol in moves:
        r, c = row + drow, col + dcol
        if (0 <= r < len(heights)) and (0 <= c < len(heights[0])):
            yield r, c


def is_low_point(heights, row, col):
    height = heights[row][col]
    for r, c in get_neighbours(heights, row, col):
        if heights[r][c] <= height:
            return False
    return True


def low_points(heights):
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if is_low_point(heights, row, col):
                yield row, col


def part1(heights):
    print(sum(heights[r][c] + 1 for r, c in low_points(heights)))


def find_basin(heights, row, col):
    basin = set()
    pending = set([(row, col,)])
    while pending:
        r, c = pending.pop()
        if heights[r][c] == 9:
            continue
        basin.add((r, c,))
        pending = pending | set(get_neighbours(heights, r, c)) - basin
    return basin


def part2(heights):
    basins = [find_basin(heights, r, c) for r, c in low_points(heights)]
    basins.sort(key=lambda basin: len(basin), reverse=True)
    print(reduce(lambda a, b: a * b, map(len, basins[:3])))


def main():
    heights = []
    for line in sys.stdin.readlines():
        heights.append([int(c) for c in line.strip()])

    part1(heights)
    part2(heights)


main()