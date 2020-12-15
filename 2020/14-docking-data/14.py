#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/14

import sys
import re

mask_re = re.compile('^mask = ([^\\n]+)')
mem_re = re.compile('mem\\[(\\d+)\\] = (\\d+)')

def mask_value(value, and_mask, or_mask):
    value = value & and_mask
    value = value | or_mask
    return value

def part_one(lines):
    memory = {}
    and_mask, or_mask = 0, 0
    max_address = 0;
    for line in lines:
        if mem_re.match(line):
            address, value = (int(x) for x in mem_re.findall(line)[0])
            memory[address] = mask_value(value, and_mask, or_mask)
            max_address = max(max_address, address)
        elif mask_re.match(line):
            new_mask = mask_re.findall(line)[0]
            and_mask = int(new_mask.replace('X', '1'), 2)
            or_mask  = int(new_mask.replace('X', '0'), 2)

    print(f'Sum of memory values: {sum(memory.values())}')

def replace_chars(address_array, mask, char, values):
    value_pos = 0
    for i in range(len(address_array)):
        if mask[i] == char:
            address_array[i] = values[value_pos]
            value_pos += 1
    return address_array

def replace_char(s, i, c):
    return s[:i] + c + s[i + 1:]

def generate_addresses(address, or_mask):
    address_array = [c for c in bin(address)[2:].zfill(len(or_mask))]
    x_count = sum(1 for c in or_mask if c == 'X')
    for i, c in enumerate(or_mask):
        if c == '1':
            address_array[i] = '1'

    for i in range(2 ** x_count):
        i_bits = [c for c in bin(i)[2:].zfill(x_count)]
        new_address_array = replace_chars(address_array[:], or_mask, 'X', i_bits)
        yield int("".join(new_address_array), 2)

def part_two(lines):
    memory = {}
    or_mask = 0
    for line in lines:
        if mem_re.match(line):
            address, value = (int(x) for x in mem_re.findall(line)[0])
            for address in generate_addresses(address, or_mask):
                memory[address] = value
        elif mask_re.match(line):
            or_mask = mask_re.findall(line)[0]

    print(f'Sum of memory values: {sum(memory.values())}')


lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]

part_one(lines)
part_two(lines)