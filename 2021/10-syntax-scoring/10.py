#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/10

import sys
from collections import deque
from collections import namedtuple
from functools import reduce

Result = namedtuple("Score", ["score", "completion"])
BRACKET_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
mapping = { '(': ')', '[': ']', '{': '}', '<': '>' }

def check_brackets(line):
    stack = deque()

    for c in line:
        if c in mapping:
            stack.append(mapping[c])
        elif c != stack.pop():
            return Result(BRACKET_SCORES[c], None)

    return Result(0, list(stack)[::-1])
    
def part1(results):
    print(sum([result.score for result in results if result.score]))    

def get_completion_score(completion):
    SCORES = {')': 1, ']': 2, '}': 3, '>': 4}
    return reduce(lambda accum, c: accum * 5 + SCORES[c], completion, 0)

def part2(results):
    all_scores = sorted([get_completion_score(r.completion) for r in results if not r.score])
    print(all_scores[len(all_scores) // 2])

def main():
    results = [check_brackets(line.strip()) for line in sys.stdin.readlines()]
    part1(results)
    part2(results)

main()