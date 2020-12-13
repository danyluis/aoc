#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/13

import sys
import re

from math import gcd
from collections import defaultdict
from functools import reduce

def read_input():
    timestamp = int(sys.stdin.readline().strip())
    ids = enumerate(sys.stdin.readline().strip().split(','))
    schedule = {int(bus) : int(t) for t, bus in ids if bus != 'x'}
    return (timestamp, schedule)

def part_one(timestamp, bus_ids):
    min_wait = float('inf')
    bus_id = -1
    for bus in bus_ids:
        if not (timestamp % bus):
            min_wait, bus_id = 0, bus
        else:
            wait = bus - (timestamp % bus)
            if wait < min_wait:
                bus_id, min_wait = bus, wait
    print(f'Part 1: bus={bus_id}, wait={min_wait}, wait * bus: {min_wait * bus_id}')

def lcm(ints):
    def pair_lcm(a, b):
        abs_a_b = abs(a * b)
        return 0 if not abs_a_b else abs_a_b // gcd(a, b)
    return reduce(lambda a, b: pair_lcm(a, b), ints)

def find_congruent_sets(schedule):
    sets = defaultdict(set)
    for bus1, i in schedule.items():
        for bus2, j in schedule.items():
            if abs(i - j) % bus2 == 0:
                sets[bus1].add(bus2)
    return sets

def pick_set_with_largest_lcm(sets):
    bus, max_lcm, selected_set = 0, 0, None
    for id, group in sets.items():
        set_lcm = lcm(group)
        if set_lcm > max_lcm:
            max_lcm = set_lcm
            bus = id
            selected_set = group
    return bus, max_lcm, selected_set

def valid_timestamp(timestamp, schedule):
    return all((timestamp + offset) % bus == 0 for bus, offset in schedule.items())

def part_two(schedule):
    print("Part 2:")
    sets = find_congruent_sets(schedule)
    bus, set_lcm, selected_set = pick_set_with_largest_lcm(sets)
    offset = schedule[bus]

    print(f'\tCongruence set={selected_set}, bus={bus}, offset={offset}, lcm={set_lcm}')

    busses_to_check = {bus : offset for bus, offset in schedule.items() if bus not in selected_set}

    timestamp = set_lcm - offset
    while not valid_timestamp(timestamp, busses_to_check):
        timestamp += set_lcm
    print(f'\tTimestamp: {timestamp}')

timestamp, schedule = read_input()
part_one(timestamp, schedule.keys())
part_two(schedule)
