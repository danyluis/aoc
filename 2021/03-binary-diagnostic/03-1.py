#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/3

import sys

def count_ones(values):
    return [sum([int(v[i]) for v in values]) for i in range(len(values[0]))]

def get_gamma(ones, count):
    return [('1' if ones[i] > (count - ones[i]) else '0') for i in range(len(ones))]#[::-1] 

def bitwise_not(bit_array):
    return ['1' if (c == '0') else '0' for c in bit_array]

def main():
    all_lines = [s.strip() for s in sys.stdin.readlines()]
    ones = count_ones(all_lines)
    print(f'ones: {ones}')

    gamma = get_gamma(ones, len(all_lines))
    epsilon = bitwise_not(gamma)

    print(f'gamma   = {gamma}')
    print(f'epsilon = {epsilon}')

    g = int(''.join(gamma), 2)
    e = int(''.join(epsilon), 2)

    print(f'gamma * epsilon = {g * e}')

main()


