#!/usr/bin/env python

import sys

expressions = (
    line.strip().replace(" ", "")
    for line in sys.stdin.readlines() if line.strip()
)

for expr in expressions:
    expr = expr.replace("+", "^")
    expr = expr.replace("*", "+")
    expr = expr.replace("^", "*")
    print(expr)