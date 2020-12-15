#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/15

numbers = [9,12,1,4,17,0,18]
size = 30000000
spoken = {}
for i, n in enumerate(numbers):
    spoken[n] = (-1 if n not in spoken else spoken[n][1], i)

for i in range(len(numbers), size):
    first, second = spoken[numbers[i-1]]
    n = 0 if first == -1 else (second - first)
    spoken[n] = (-1 if n not in spoken else spoken[n][1], i)
    numbers.append(n)
    if i % 1000000 == 0:
        print(f'numbers[{i}] = {numbers[i]}')

print(f'2020th number = {numbers[2019]}')
print(f'{size}th number = {numbers[size - 1]}')