#!/usr/bin/env python

# Advent of Code 2015
# https://adventofcode.com/2015/day/4

import sys
import hashlib

password = 'ckczppom'

def find_integer_suffix_for(digest_prefix):
    hexdigest = None
    i = 1
    while True:
        hexdigest = hashlib.md5(bytes(password + str(i), encoding='ascii')).hexdigest()
        if hexdigest[:len(digest_prefix)] == digest_prefix:
            break
        i += 1
    return i, hexdigest

for prefix in ('00000', '000000'):
    i, hexdigest = find_integer_suffix_for(prefix)
    print(f'i = {i}, hexdigest = {hexdigest}')