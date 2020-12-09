#!/usr/bin/env python

# Advent of Code 2015
# https://adventofcode.com/2015/day/3

import sys

moves = {
    '^' : (-1, 0),
    '>' : (0, 1),
    '<' : (0, -1),
    'v' : (1, 0)
}

def follow_route(steps):
    curr = (0, 0)
    visited = {curr}
    for d in steps:
        move = moves[d]
        curr = (curr[0] + move[0], curr[1] + move[1])
        visited.add(curr)
    return visited

def both_deliver(steps):
    santa = [steps[i] for i in range(0, len(steps), 2)]
    robot = [steps[i] for i in range(1, len(steps), 2)]
    houses = follow_route(santa) | follow_route(robot)
    return houses

for line in sys.stdin:
    print(f'Only Santa: {len(follow_route(line))}')
    print(f'Both Deliver: {len(both_deliver(line))}')

