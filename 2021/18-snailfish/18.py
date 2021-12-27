#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/18

import sys
import re
from collections import namedtuple

int_re = re.compile("\\d+")
pair_re = re.compile('(\\[(\\d+),(\\d+)\\])')
explode_re = re.compile('(\\[[^\\[]*){4}(\\[(\\d+),(\\d+)\\])')
Explodable = namedtuple("Explodable", ["string", "start", "end", "left", "right"])
Splittable = namedtuple("Splittable", ["string", "start", "end", "value"]) 
Replacement = namedtuple("Replacement", ["start", "end", "value"])

def replace(string, start, end, replacement):
	return string[:start] + replacement + string[end:]

def replace_all(string, replacements):
	in_order = sorted(replacements, key=lambda repl: repl.start)
	result, offset = "", 0
	for start, end, value in in_order:
		result += string[offset:start] + value
		offset = end
	return result + string[offset:]

def find_last_int(s, start, end):
	m = None
	for m in int_re.finditer(s, pos=start, endpos=end):
		pass
	return m

def find_first_int(s, start, end, f=None):
	for m in int_re.finditer(s, pos=start, endpos=end):
		if not f:
			return m
		elif f(int(m.group(0))):
			return m
	else:
		return None

def bracket_levels(s):
	return sum(1 if c == '[' else -1 for c in s if c in '[]')

def find_explodable(s):
	for m in pair_re.finditer(s):
		if bracket_levels(s[0:m.span()[0] + 1]) >= 5:
			start, end = m.span()
			return Explodable(s, start, end, int(m.group(2)), int(m.group(3)))
	return None

def explode(explodable):
	s, start, end, left, right = explodable
	replacements = [Replacement(start, end, '0')]

	if (lmatch := find_last_int(s, 0, start)):
		i = str(left if not lmatch else int(lmatch.group(0)) + left)
		replacements.append(Replacement(lmatch.span()[0], lmatch.span()[1], i))

	if (rmatch := find_first_int(s, end, len(s))):
		j = str(right if not rmatch else int(rmatch.group(0)) + right)
		replacements.append(Replacement(rmatch.span()[0], rmatch.span()[1], j))

	return replace_all(s, replacements)

def find_splittable(s):
	if not (m := find_first_int(s, 0, len(s), lambda i: i >= 10)):
		return None
	return Splittable(s, m.span()[0], m.span()[1], int(m.group(0)))

def split(splittable):
	s, start, end, value = splittable
	return replace(s, start, end, f'[{value // 2},{value // 2 + value % 2}]')

def magnitude_rec(string, pos=0):
	if pos >= len(string):
		return 0, pos

	if string[pos] == "[":
		left, pos = magnitude_rec(string, pos + 1)
		right, pos = magnitude_rec(string, pos + 1)
		return 3 * left + 2 * right, pos + 1
	else:
		start, end = int_re.match(string[pos]).span()
		return int(string[pos + start:pos + end]), pos + end

def sum_magnitude(lines):
	s, i = lines[0], 0
	for i in range(1, len(lines)):
		s = f'[{s},{lines[i]}]'
		while True:
			while exp := find_explodable(s):
				s = explode(exp)
			if spl := find_splittable(s):
				s = split(spl)
			else:
				break
	mag, pos = magnitude_rec(s)
	return mag

def max_pair_sum_magnitude(lines):
	mx = float('-inf')
	for i in range(len(lines) - 1):
		for j in range(i + 1, len(lines)):
			mx = max(mx, sum_magnitude([lines[i], lines[j]]), sum_magnitude([lines[j], lines[i]]))
	return mx

def main():
	lines = [s.strip() for s in sys.stdin.readlines()]
	print(f'sum magnitude: {sum_magnitude(lines)}')
	print(f'max pair sum magnitude: {max_pair_sum_magnitude(lines)}')

main()