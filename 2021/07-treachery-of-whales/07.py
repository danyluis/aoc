#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/7

import sys
from collections import Counter

def linear_fuel(a, b):
    return abs(a - b)

def sn_fuel(a, b):
    d = abs(a - b)
    return (d * (d + 1)) // 2

def total_fuel_to(i, crab_cter, compute_fuel):
    return sum(compute_fuel(pos, i) * count for pos, count in crab_cter.items())

def linear_search(crab_cter, compute_fuel):
    min_fuel = float('inf')
    for i in range(min(crab_cter), max(crab_cter) + 1):
        min_fuel = min(min_fuel, total_fuel_to(i, crab_cter, compute_fuel))
    return min_fuel

def binary_search(crab_cter, compute_fuel):
    left, right = min(crab_cter), max(crab_cter)
    fuel_left = total_fuel_to(left, crab_cter, compute_fuel)
    fuel_right = total_fuel_to(right, crab_cter, compute_fuel)
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if fuel_left <= fuel_right:
            right = mid
            fuel_right = total_fuel_to(right, crab_cter, compute_fuel)
        elif fuel_right < fuel_left:
            left = mid
            fuel_left = total_fuel_to(left, crab_cter, compute_fuel)
    return min(fuel_left, fuel_right)

def main():
    crab_cter = Counter([int(s.strip()) for s in sys.stdin.readline().strip().split(',')])
    print('linear_search:')
    print(f'\tLinear fuel: {linear_search(crab_cter, linear_fuel)}')
    print(f'\tSN fuel: {linear_search(crab_cter, sn_fuel)}')
    print('\nbinary_search:')
    print(f'\tLinear fuel: {binary_search(crab_cter, linear_fuel)}')
    print(f'\tSN fuel: {binary_search(crab_cter, sn_fuel)}')


main()