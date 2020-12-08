#!/usr/bin/env python

import sys

def required_paper(a, b, c):
    a, b, c = sorted([a, b, c])
    return 2 * (a * b + b * c + a * c) + a * b

def required_ribbon(a, b, c):
    a, b, c = sorted([a, b, c])
    return 2 * (a + b) + a * b * c

total_paper, total_ribbon = 0, 0
for line in sys.stdin:
    a, b, c = [int(part) for part in line.split('x')]
    total_paper += required_paper(a, b, c)
    total_ribbon += required_ribbon(a, b, c)

print(f'Required paper: {total_paper}')
print(f'Required ribbon: {total_ribbon}')