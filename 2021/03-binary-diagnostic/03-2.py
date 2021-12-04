#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/3

import sys

def count_ones(values):
    return [sum([int(v[i]) for v in values]) for i in range(len(values[0]))]


def find_metric(values, f):
    for i in range(len(values[0])):
        ones = count_ones(values)
        selector = f(ones, values, i)
        new_values = [v for v in values if v[i] == selector]
        if len(new_values) == 0:
            continue
        values = new_values
        if len(new_values) == 1:
            break
    return int(values[0], 2)


def get_ogr(ones, values, i):
    return '1' if (ones[i] >= (len(values) - ones[i])) else '0'


def get_csr(ones, values, i):
    return '1' if (ones[i] < (len(values) - ones[i])) else '0'


def main():
    length = 0
    all_lines = [s.strip() for s in sys.stdin.readlines()]
    ones = count_ones(all_lines)
    ogr = find_metric(all_lines, get_ogr)
    csr = find_metric(all_lines, get_csr)

    print(f'oxygen generator rating: {ogr}')
    print(f'CO2 scrubber rating:     {csr}')
    print(f'org * csr = {ogr * csr}')


main()