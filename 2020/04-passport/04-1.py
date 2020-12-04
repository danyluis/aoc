#!/usr/bin/env python
import sys
import re


def read_passports():
    fields = []
    for line in sys.stdin:
        line = line.strip()
    
        if not line:
            yield(fields)
            fields = []
        else:
            fields.extend([f.strip() for f in line.split(" ")])

    if fields:
        yield fields

expected = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
valid = 0

for passport in read_passports():
    existing = 0
    for field in passport:
        print(field)
        name, value = [i.strip() for i in field.split(":")]
        if name in expected and value:
            existing += 1
    if existing == 7:
        valid += 1
        print(f'{valid} valid!')
    else:
        print(f'{valid} invalid!')

    print()

print(f'Total valid passports: {valid}')
