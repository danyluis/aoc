#!/usr/bin/env python
import sys
from datetime import datetime

def read_seat_codes():
    return (seat_code(l.strip()) for l in sys.stdin.readlines())


def seat_code(strcode):
    return int("".join(["1" if c in ("B", "R") else "0" for c in strcode]), 2)


def solve_using_sn(seat_codes):

    def sn(n):
        return (n * (n + 1)) >> 1

    return sn(max(seat_codes)) - sn(min(seat_codes) - 1) - sum(seat_codes)


def solve_using_set(seat_codes):
    for seat in range(min(seat_codes), max(seat_codes) + 1):
        if seat not in seat_codes:
            return seat


def run(f, seat_codes):
    start = datetime.now()
    seat = f(seat_codes)
    end = datetime.now()
    print(f'Your seat is {seat}')
    print(f'Time for {f.__name__}: {end - start}\n')


seat_codes = set(read_seat_codes())
for f in (solve_using_sn, solve_using_set):
    run(f, seat_codes)
