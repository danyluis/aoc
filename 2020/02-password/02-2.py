#!/usr/bin/env python
import sys
from collections import Counter

valid = 0
for line in sys.stdin:
    times, letter, password = line.split(" ")
    i, j = [int(s) - 1 for s in times.split("-")]
    letter = letter[0]
    if (password[i] == letter) ^ (password[j] == letter):
        valid += 1

print(f'Valid passwords {valid}')