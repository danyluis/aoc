#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/17

import sys
import re

regex = re.compile('target area: x=(-?\\d+)\\.\\.(-?\\d+), y=(-?\\d+)\\.\\.(-?\\d+)')
x1, x2, y1, y2 = [int(s) for s in regex.match(sys.stdin.readline().strip()).groups()]
x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = max(y1, y2), min(y1, y2)
print(f'parameters ({x1}, {x2}), ({y1}, {y2})')

def hits(vx, vy):
	x = y = maxy = 0
	while True:
		if x1 <= x <= x2 and y1 >= y >= y2:
			return (True, maxy)

		x, y = x + vx, y + vy
		maxy = max(maxy, y)

		if x > x2 or y < y2:
			return (False, None)

		vx -= 0 if not vx else vx // abs(vx)
		vy -= 1

maxy = vel_count = 0
for vx in range(1, x2 + 1):
	for vy in range(-abs(y2), 2 * abs(y2) + 1, 1):
		does_hit, mxy = hits(vx, vy)
		if does_hit:
			maxy = max(maxy, mxy)
			vel_count += 1

print(f'maxy {maxy}')
print(f'#velocities {vel_count}')
