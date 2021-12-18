#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/16

import sys
from functools import reduce

class Reader:
	functions = {
		0: sum,
		1: lambda arr: reduce(lambda a, b: a * b, arr, 1),
		2: min,
		3: max,
		5: lambda arr: int(arr[0] > arr[1]),
		6: lambda arr: int(arr[0] < arr[1]),
		7: lambda arr: int(arr[0] == arr[1])
	}

	def __init__(self, s):
		self.string = s if set(s) == {'0', '1'} else "".join(bin(int(c, 16))[2:].zfill(4) for c in s)
		self.pos = 0
		self.version_sum = 0

	def finished(self):
		return self.pos >= len(self.string)

	def read_n(self, n):
		s = self.string[self.pos : self.pos + n]
		self.pos += n
		return s if self.pos <= len(self.string) else None

	def read_int(self, n):
		return None if (s := self.read_n(n)) == None else int(s, 2)

	def read_version(self):
		if (v := self.read_int(3)) != None:
			self.version_sum += v
		return v

	def read_type(self):
		return None if (t := self.read_int(3)) == None else t

	def literal(self):
		ret = s = self.read_n(5)
		while s[0] == '1':
			ret += (s := self.read_n(5))[:1]
		return int(ret, 2)

	def operate(self, operator):
		if self.read_int(1):
			values = [self.solve() for _ in range(self.read_int(11))]
		else:
			nxt = self.read_n(self.read_int(15))
			reader = Reader(nxt)
			values = []
			while not reader.finished():
				values.append(reader.solve())
			self.version_sum += reader.version_sum

		return self.functions[operator](values)

	def solve(self):
		while self.read_version() != None:
			op = self.read_type()
			return None if op == None else self.literal() if op == 4 else self.operate(op)

if len(sys.argv) > 1:
	r = Reader(sys.argv[1])
else:
	r = Reader(sys.stdin.readline().strip())

print(f'solve: {r.solve()}')
print(f'version_sum: {r.version_sum}')
