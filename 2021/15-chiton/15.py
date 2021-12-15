#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/15

import sys
from collections import defaultdict
from collections import namedtuple
import heapq

MAX = float('inf')

def cells_around(cell, matrix):
    row, col = cell
    for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        r, c = row + dr, col + dc
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            yield (r, c,)

def all_cells(matrix):
    return ((r, c,) for c in range(len(matrix[0])) for r in range(len(matrix)))

def distances_around(cell, matrix):
    for r, c in cells_around(cell, matrix):
        yield ((r, c,), matrix[r][c],)
        
def tile_cave(cave, times=5):
    h, w = len(cave), len(cave[0])
    return [[((cave[r % h][c % w] - 1 + r // h + c // w) % 9) + 1 for c in range(w * times)]
        for r in range(h * times) ]

def dijkstra(matrix, source=(0, 0,)):
    dist = {cell: MAX for cell in all_cells(matrix)}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        base_distance, cell = heapq.heappop(heap)
        if base_distance <= dist[cell]:
            for neighbour, d_to_neighbour in distances_around(cell, matrix):
                d = base_distance + d_to_neighbour
                if d < dist[neighbour]:
                    dist[neighbour] = d
                    heapq.heappush(heap, (d, neighbour))

    dest = max(dist.keys())
    print(f'distance from {source} to {dest}: {dist[dest]} ')


cave = [[int(i) for i in line.strip()] for line in sys.stdin.readlines()]

print('small')
dijkstra(cave)

print('\nbig')
dijkstra(tile_cave(cave))
