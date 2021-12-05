#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/5

import sys
import re
from collections import namedtuple

Segment = namedtuple("Segment", ["r1", "c1", "r2", "c2"])

def build_board(segments, height, width):
    board = [[0] * width for i in range(height)]

    for s in segments:
        rdiff = abs(s.r1 - s.r2)
        cdiff = abs(s.c1 - s.c2)

        if rdiff and cdiff:
            continue

        rstep = 0 if not rdiff else (1 if s.r2 > s.r1 else -1)
        cstep = 0 if not cdiff else (1 if s.c2 > s.c1 else -1)

        row, col = s.r1, s.c1
        for i in range(max(rdiff, cdiff) + 1):
            board[row][col] += 1
            row += rstep
            col += cstep

    return board

def count_dangerous(board):
    count = 0;
    for row in range(len(board)):
        for col in range(len(board[0])):
            count += 1 if board[row][col] > 1 else 0
    return count

def main():
    reg = re.compile('(\\d+),(\\d+) -> (\\d+),(\\d+)')
    maxx, maxy = 0, 0
    segments = set()
    for line in sys.stdin.readlines():
        r1, c1, r2, c2 = [int(s) for s in reg.search(line.strip()).groups()]
        maxy = max(maxy, r1, r2)
        maxx = max(maxx, c1, c2)
        segments.add(Segment(r1, c1, r2, c2))

    board = build_board(segments, maxy + 1, maxx + 1)
    print(f'#dangerous points: {count_dangerous(board)}')


main()