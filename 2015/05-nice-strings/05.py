#!/usr/bin/env python

# Advent of Code 2015
# https://adventofcode.com/2015/day/5

import sys
import re

def count_vowels(s):
    return sum(1 for c in s if c in {'a', 'e', 'i', 'o', 'u'})

def has_repetitions(s):
    return any(s[i] == s[i+1] for i in range(len(s) - 1))

def has_forbidden_pairs(s):
    return re.search("ab|cd|pq|xy", s) is not None

def first_part(lines):
    return sum(1 for s in lines if
        count_vowels(s) >= 3 and
        has_repetitions(s) and
        not has_forbidden_pairs(s))

double_pair_re = re.compile('(?P<pair>..).*(?P=pair)')
repeated_1_char_apart = re.compile('(?P<letter>.).(?P=letter)')

def second_part(lines):
    return sum(1 for s in lines if
        double_pair_re.search(s) is not None and
        repeated_1_char_apart.search(s) is not None)

lines = [line.strip() for line in sys.stdin.readlines()]
print(f'(1st) Nice lines: {first_part(lines)}')
print(f'(2nd) Nice lines: {second_part(lines)}')
