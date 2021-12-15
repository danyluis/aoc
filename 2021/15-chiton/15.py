#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/15

import sys
from collections import defaultdict
from collections import namedtuple
import heapq

MAX = float('inf')

def cells_around(cell, height, width):
    row, col = cell
    for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        r, c = row + dr, col + dc
        if 0 <= r < height and 0 <= c < width:
            yield (r, c,)

def all_cells(height, width):
    return ((r, c,) for c in range(width) for r in range(height))

def risk(matrix, row, col):
    h, w = len(matrix), len(matrix[0])
    return ((matrix[row % h][col % w] - 1 + row // h + col // w) % 9) + 1

def risks_around(cell, matrix, height, width):
    for cell in cells_around(cell, height, width):
        yield (cell, risk(matrix, *cell))

def dijkstra(matrix, source=(0, 0,), tiles=1):
    height, width = len(matrix) * tiles, len(matrix[0]) * tiles
    dist = {cell: MAX for cell in all_cells(height, width)}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        base_distance, cell = heapq.heappop(heap)
        if base_distance <= dist[cell]:
            for neighbour, d_to_neighbour in risks_around(cell, matrix, height, width):
                d = base_distance + d_to_neighbour
                if d < dist[neighbour]:
                    dist[neighbour] = d
                    heapq.heappush(heap, (d, neighbour))

    dest = max(dist.keys())
    print(f'total risk from {source} to {dest}: {dist[dest]} ')


cave = [[int(i) for i in line.strip()] for line in sys.stdin.readlines()]

print('small')
dijkstra(cave)

print('\nbig')
dijkstra(cave, source=(0, 0), tiles=5)
