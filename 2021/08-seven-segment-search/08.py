#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/8

import sys
from collections import namedtuple

Line = namedtuple("Line", ["signals", "digits"])

class Segments:
    def __init__(self, line):
        self.line = line
        self.number_to_str = {}
        self.initialize()

    def initialize(self):
        self.find_by_length()
        self.find(length=6, which=6, union_with=1, equals_to=8)
        self.find(length=5, which=3, union_with=1, equals_to=3)
        self.find(length=6, which=9, union_with=3, equals_to=9)
        self.find(length=6, which=0, union_with=0, equals_to=0)
        self.find(length=5, which=5, union_with=6, equals_to=6)
        self.find(length=5, which=2, union_with=6, equals_to=8)
        # print(f'number_to_str({len(self.number_to_str)}): {self.number_to_str}')

    def find_by_length(self):
        length_to_digit = {2 : 1, 3: 7, 4: 4, 7: 8}
        for s in self.line.signals:
            length = len(s)
            if length in length_to_digit:
                self.number_to_str[length_to_digit[length]] = s

    def find(self, length, which, union_with, equals_to):
        existing = self.number_to_str.values()
        for s in self.line.signals:
            if len(s) != length or s in existing:
                continue
            if self.add(s, self.get_or_default(union_with, s)) == self.get_or_default(equals_to, s):
                self.number_to_str[which] = s
                break

    def add(self, *strings):
        return "".join(sorted(set("".join(strings))))

    def get_or_default(self, which, str):
        if which in self.number_to_str:
            return self.number_to_str[which]
        return str

    def solve(self):
        str_to_number = {v: k for k, v in self.number_to_str.items()}
        value = 0
        for str_digit in self.line.digits:
            value = (value * 10) + str_to_number[str_digit]
        return value


def part1(lines):
    count = 0
    for line in lines:
        for s in line.digits:
            if len(s) in (2, 4, 3, 7):
                count  += 1
    print(f'Part 1 -- count: {count}')


def part2(lines):
    total = 0
    for line in lines:
        total += Segments(line).solve()
    print(f'Part 2 -- total: {total}')


def signature(string):
    return "".join(sorted(string))


def break_line(line):
    signals, digits = line.split("|")
    return Line(
        [signature(s.strip()) for s in signals.strip().split(" ")],
        [signature(s.strip()) for s in digits.strip().split(" ")])


def main():
    lines = [break_line(line) for line in sys.stdin.readlines()]
    part1(lines)
    part2(lines)


main()