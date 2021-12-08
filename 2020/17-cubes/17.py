#!/usr/bin/env python

import sys


def min_coords(cube):
    minx, miny, minz = float('inf'), float('inf'), float('inf')
    for x, y, z in cube:
        minx, miny, minz = min(x, minx), min(y, miny), min(z, minz)
    return minx, miny, minz

def max_coords(cube):
    maxx, maxy, maxz = float('-inf'), float('-inf'), float('-inf')
    for x, y, z in cube:
        maxx, maxy, maxz = max(x, maxx), max(y, maxy), max(z, maxz)
    return maxx, maxy, maxz

def count_active_around(cube, x, y, z):
    cnt = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i, j, k) == (x, y, z):
                    continue
                if (i, j, k) in cube:
                    cnt += 1
    return cnt

def read_cube():
    cube = set()
    for i, line in enumerate(sys.stdin.readlines()):
        line = line.strip()
        for j, c in enumerate(line):
            if c == '#':
                cube.add((i, j, 0))
    return cube

cube = read_cube()
for step in range(6):
    minx, miny, minz = min_coords(cube)
    maxx, maxy, maxz = max_coords(cube)

    to_activate = set()
    to_deactivate = set()
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                active_around = count_active_around(cube, x, y, z)
                if (x, y, z) in cube:
                    if active_around not in {2, 3}:
                        to_deactivate.add((x, y, z))
                else:
                    if active_around == 3:
                        to_activate.add((x, y, z))
    cube -= to_deactivate
    cube |= to_activate

print(len(cube))