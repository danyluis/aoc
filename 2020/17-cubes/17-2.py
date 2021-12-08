#!/usr/bin/env python

import sys


def min_coords(cube):
    minx, miny, minz, mint = float('inf'), float('inf'), float('inf'), float('inf')
    for x, y, z, t in cube:
        minx, miny, minz, mint = min(x, minx), min(y, miny), min(z, minz), min(t, mint)
    return minx, miny, minz, mint

def max_coords(cube):
    maxx, maxy, maxz, maxt = float('-inf'), float('-inf'), float('-inf'), float('-inf')
    for x, y, z, t in cube:
        maxx, maxy, maxz, maxt = max(x, maxx), max(y, maxy), max(z, maxz), max(t, maxt)
    return maxx, maxy, maxz, maxt

def count_active_around(cube, x, y, z, t):
    cnt = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
               for l in range(t - 1, t + 2):
                if (i, j, k, l) == (x, y, z, t):
                    continue
                if (i, j, k, l) in cube:
                    cnt += 1
    return cnt

def read_cube():
    cube = set()
    for i, line in enumerate(sys.stdin.readlines()):
        line = line.strip()
        for j, c in enumerate(line):
            if c == '#':
                cube.add((i, j, 0, 0))
    return cube

cube = read_cube()
for step in range(6):
    minx, miny, minz, mint = min_coords(cube)
    maxx, maxy, maxz, maxt = max_coords(cube)

    to_activate = set()
    to_deactivate = set()
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
               for t in range(mint - 1, maxt + 2):
                    active_around = count_active_around(cube, x, y, z, t)
                    if (x, y, z, t) in cube:
                        if active_around not in {2, 3}:
                            to_deactivate.add((x, y, z, t))
                    else:
                        if active_around == 3:
                            to_activate.add((x, y, z, t))
    cube -= to_deactivate
    cube |= to_activate

print(len(cube))