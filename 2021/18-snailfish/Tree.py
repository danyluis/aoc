# Advent of Code 2021
# https://adventofcode.com/2021/day/18

import sys
import re
from collections import deque
from collections import namedtuple

number = re.compile('\\d+')

class Tree:
	def __init__(self, left, right, value):
		self.left = left
		self.right = right
		self.value = value

	def magnitude(self):
		if self.value is None:
			return 3 * self.left.magnitude() + 2 * self.right.magnitude()
		else:
			return self.value

def __read_tree(string, pos=0):
	if pos >= len(string):
		return None, pos

	if string[pos] == "[":
		left, pos = __read_tree(string, pos + 1)
		right, pos = __read_tree(string, pos + 1)
		return Tree(left, right, None), pos + 1
	else:
		start, end = number.match(string[pos]).span()
		return Tree(None, None, int(string[pos + start:pos + end])), pos + end

def read_tree(string):
	tree, pos = __read_tree(string)
	return tree
