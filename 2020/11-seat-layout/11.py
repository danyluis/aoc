#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/11

import sys
import copy

FLOOR = "."
OCCUPIED = "#"
EMPTY = "L"

directions = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)


def count_occupied_around(layout, i, j):
    occupied, height, width = 0, len(layout), len(layout[0])
    for row_move, col_move in directions:
        a, b = i + row_move, j + col_move
        if 0 <= a < height and 0 <= b < width:
            occupied += layout[a][b] == OCCUPIED
    return occupied


def count_visible_occupied(layout, i, j):
    occupied, height, width = 0, len(layout), len(layout[0])
    for row_move, col_move in directions:
        a, b = i + row_move, j + col_move
        while 0 <= a < height and 0 <= b < width:
            state = layout[a][b]
            if state != FLOOR:
                occupied += state == OCCUPIED
                break
            else:
                a, b = a + row_move, b + col_move
    return occupied


def apply_rules(layout, i, j, occupied_threshold, seat_count_f):
    pre = layout[i][j]

    if pre == FLOOR:
        return pre

    occupied_count = seat_count_f(layout, i, j)

    if pre == OCCUPIED and occupied_count >= occupied_threshold:
        return EMPTY

    if pre == EMPTY and occupied_count == 0:
        return OCCUPIED

    return pre


def round(layout, occupied_threshold, seat_count_f):
    changed, height, width = False, len(layout), len(layout[0])
    new_layout = copy.deepcopy(layout)
    for row in range(height):
        for col in range(width):
            new_layout[row][col] = apply_rules(layout, row, col, occupied_threshold, seat_count_f)
            changed = changed or (layout[row][col] != new_layout[row][col])
    return (changed, new_layout)


def change_until_stable(layout, occupied_threshold, seat_count_f):
    while True:
        changed, new_layout = round(layout, occupied_threshold, seat_count_f)
        if not changed:
            break
        layout = new_layout
    return layout


def read_seat_layout():
    return [[c for c in line.strip()] for line in sys.stdin.readlines() if line.strip()]


original = read_seat_layout()

layout = change_until_stable(copy.deepcopy(original), 4, count_occupied_around)
occupied = sum(sum(1 for seat in row if seat == OCCUPIED) for row in layout)
print(f'Part 1: #Seats occupied: {occupied}')

layout = change_until_stable(copy.deepcopy(original), 5, count_visible_occupied)
occupied = sum(sum(1 for seat in row if seat == OCCUPIED) for row in layout)
print(f'Part 2: #Seats occupied: {occupied}')
