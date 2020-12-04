#!/usr/bin/env python
import sys
from collections import Counter

for line in sys.stdin:
    cter = Counter(line)
    print(cter["("] - cter[")"])
