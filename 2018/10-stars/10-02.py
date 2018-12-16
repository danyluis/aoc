# Advent of Code 2018
# https://adventofcode.com/2018/day/10
# Dany Farina (danyluis@gmail.com)

from re import *
from sys import *
from collections import *

DIM = 70

def dashboard(points):
    minx, miny = float("inf"), float("inf")
    maxx, maxy = float("-inf"), float("-inf")

    stars = set([(x, y) for x, y, h, v in points])
    for x, y, h, v in points:
        maxx = max(maxx, x)
        minx = min(minx, x)
        maxy = max(maxy, y)
        miny = min(miny, y)

    if abs(maxx - minx) < DIM and abs(miny - maxy) < DIM:
        return "\n".join(
            [
                "".join(
                    ["*" if (j, i) in stars else " " for j in xrange(minx, maxx + 1)]
                ) for i in xrange(miny, maxy + 1)
            ]
        )
    return ""

def move(points):
    for i in xrange(len(points)):
        h, v = points[i][2:]
        points[i][0] += h
        points[i][1] += v

expr   = compile(r"position=<\s*([-\d]+),\s*([-\d]+)>\s*velocity=<\s*([-\d]+),\s*([-\d]+)>")
points = [[int(i) for i in expr.split(line.strip())[1:5]] for line in stdin.readlines()]

for i in xrange(20000):
    board = dashboard(points)
    if board:
        print "{}\n{}\n\n".format(i, board)
    move(points)