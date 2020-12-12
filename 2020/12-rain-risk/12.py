#!/usr/bin/env python

import sys
import re

move_re = re.compile("(\\w)(\\d+)")

quadrant_sign = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

moves = {
    'N' : (0, 1),
    'S' : (0, -1),
    'E' : (1, 0),
    'W' : (-1, 0)
}

def sign(direction):
    if direction == 'L':
        return -1
    if direction == 'R':
        return 1
    return 0


def rotate_ship(direction, side, deg):
    directions = ('N', 'E', 'S', 'W')
    return directions[(directions.index(direction) + (sign(side) * (deg // 90))) % 4]


def advance(position, direction, steps):
    x, y = position
    dx, dy = moves[direction]
    return (x + steps * dx, y + steps * dy)


def part_one(instructions):
    direction = 'E'
    ship = (0, 0)
    start_x, start_y = ship
    for line in instructions:
        move, steps = move_re.findall(line)[0]
        steps = int(steps)

        if move in ('L', 'R'):
            direction = rotate_ship(direction, move, steps)
        elif move == 'F':
            ship = advance(ship, direction, steps)
        else:
            ship = advance(ship, move, steps)

    end_x, end_y = ship
    print(f'Part 1: Manhattan distance: {abs(end_x - start_x) + abs(end_y - start_y)}')


def quadrant(waypoint):
    x, y = waypoint
    sx, sy = (1 if not x else (x / abs(x)), 1 if not y else (y / abs(y)))
    return quadrant_sign.index((sx, sy))


def rotate_waypoint(waypoint, side, degrees):
    if waypoint == (0, 0):
        return waypoint

    curr_quadrant = quadrant(waypoint)
    new_quadrant = (curr_quadrant + (sign(side) * degrees // 90)) % 4
    new_sx, new_sy = quadrant_sign[new_quadrant]

    x, y = waypoint
    if abs((degrees // 90) % 2):
        y, x = waypoint

    return (new_sx * abs(x), new_sy * abs(y))


def advance_to_waypoint(position, waypoint, steps):
    x, y = position
    dx, dy = waypoint
    return (x + steps * dx, y + steps * dy)


def part_two(instructions):
    ship = (0, 0)
    waypoint = (10, 1)

    start_x, start_y = ship
    for line in instructions:
        move, steps = move_re.findall(line)[0]
        steps = int(steps)

        if move in ('L', 'R'):
            waypoint = rotate_waypoint(waypoint, move, steps)
        elif move == 'F':
            ship = advance_to_waypoint(ship, waypoint, steps)
        else:
            waypoint = advance(waypoint, move, steps)

    end_x, end_y = ship
    print(f'Part 2: Manhattan distance: {abs(end_x - start_x) + abs(end_y - start_y)}')


instructions = [line.strip() for line in sys.stdin.readlines() if line.strip()]
part_one(instructions)
part_two(instructions)