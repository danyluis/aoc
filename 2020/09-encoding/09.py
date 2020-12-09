#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/9

import sys
from collections import Counter

PREAMBLE_LENGTH = 25

def is_sum_of_two_in(number, occurrences):
    for a in occurrences:
        b = number - a
        if occurrences[b] > 0:
            if a != b or occurrences[a] > 1:
                return True
    else:
        return False

def find_invalid(numbers):
    occurrences = Counter(numbers[:PREAMBLE_LENGTH])
    for i in range(PREAMBLE_LENGTH, len(numbers)):
        if not is_sum_of_two_in(numbers[i], occurrences):
            return numbers[i]
        outgoing, incoming = numbers[i - PREAMBLE_LENGTH], numbers[i]
        occurrences[outgoing] -= 1
        occurrences[incoming] += 1
    return None

def find_sum_range(numbers, invalid):
    number_range = None
    for l in range(2, len(numbers)):
        s = sum(numbers[:l])
        if s == invalid:
            return numbers[:l]

        for i in range(1, len(numbers) - l):
            s += numbers[i + l - 1] - numbers[i - 1]
            if s == invalid:
                return numbers[i : l + i]

    return None

numbers = [int(s.strip()) for s in sys.stdin.readlines()]

invalid = find_invalid(numbers)
print(f'{invalid} is not sum of the previous {PREAMBLE_LENGTH} elements')

number_range = find_sum_range(numbers, invalid)
print(f'range={number_range}, sum={sum(number_range)}, min={min(number_range)}, max={max(number_range)}, max_min_sum={max(number_range) + min(number_range)}')

