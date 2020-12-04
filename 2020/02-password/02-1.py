#!/usr/bin/env python
import sys
from collections import Counter

valid = 0
for line in sys.stdin:
    times, letter, password = line.split(" ")
    mn, mx = [int(s) for s in times.split("-")]
    letter = letter[0]
    cter = Counter(password)
    if mn <= cter[letter] <= mx:
        valid += 1

print(f'Valid passwords: {valid}')