#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/11

import sys
import copy

def neighbours(matrix, r, c):
    height, width = len(matrix), len(matrix[0])
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        row, col = r + dr, c + dc
        if (0 <= row < height) and (0 <= col < width):
            yield (row, col,)

def all_cells(matrix):
    return ((r, c,) for c in range(len(matrix[0])) for r in range(len(matrix)))

def apply_func(matrix, f):
    for r, c in all_cells(matrix):
        matrix[r][c] = f(matrix, r, c)

def flash_octopi(octopi, check_on_step):
    height, width, flashes = len(octopi), len(octopi[0]), 0
    for s in range(1, 1000):
        apply_func(octopi, lambda m, r, c: m[r][c] + 1)
        flashed = {(r, c,) for r, c in all_cells(octopi) if octopi[r][c] > 9}

        just_flashed = set(flashed)
        while just_flashed:
            flashed_neighbours = set()
            for r, c in just_flashed:
                neighs = set(neighbours(octopi, r, c))
                apply_func(octopi, lambda m, r, c: m[r][c] + 1 if (r, c,) in neighs else m[r][c])
                flashed_neighbours |= set(filter(lambda r: octopi[r[0]][r[1]] > 9, neighs - flashed))
            just_flashed = flashed_neighbours
            flashed |= flashed_neighbours

        if all(octopi[r][c] > 9 for r, c in all_cells(octopi)):
            print(f'step all zero: {s}')
            break

        apply_func(octopi, lambda m, r, c: m[r][c] if m[r][c] <= 9 else 0)

        flashes += len(flashed)
        if (s == check_on_step):
            print(f'flashes on step {check_on_step}: {flashes}')

flash_octopi([[int(c) for c in line.strip()] for line in sys.stdin.readlines()], check_on_step=100)

