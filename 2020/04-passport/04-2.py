#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/4

import sys
import re

def read_passports():
    fields = []
    for line in sys.stdin:
        line = line.strip()

        if not line:
            yield fields
            fields = []
        else:
            for field in [f.strip() for f in line.split(" ")]:
                fields.append(field)
    if fields:
        yield fields

def is_number(s):
    return all([i.isdigit() for i in s])


def is_valid_number(s, mn, mx, l):
    if len(s) != l:
        return False
    if not is_number(s):
        return False
    val = int(s)
    if val < mn or val > mx:
        return False
    return True


def is_valid_birth_year(s):
    return is_valid_year(s, 1920, 2002)


def is_valid_issue_year(s):
    return is_valid_year(s, 2010, 2020)


def is_valid_expiration_year(s):
    return is_valid_year(s, 2020, 2030)


def is_valid_year(s, mn, mx):
    return is_valid_number(s, mn, mx, 4)


def is_valid_height(s):
    if re.match('\\d+cm', s):
        dig = s[:len(s)-2]
        return is_valid_number(dig, 150, 193, 3)

    if re.match('\\d+in', s):
        dig = s[:len(s)-2]
        return is_valid_number(dig, 59, 76, 2)

    return False


def is_valid_hair_color(s):
    if s[0] != "#":
        return False

    s = s[1:]
    if len(s) != 6:
        return False

    if not re.match('[0-9a-f]+', s):
        return False

    return True


def is_valid_eye_color(s):
    return s in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def is_valid_passport_id(s):
    return is_valid_number(s, 0, 999999999, 9)


def is_valid_country_id(s):
    return True


validation_methods = {
    'byr': is_valid_birth_year,
    'iyr': is_valid_issue_year,
    'eyr': is_valid_expiration_year,
    'hgt': is_valid_height,
    'hcl': is_valid_hair_color,
    'ecl': is_valid_eye_color,
    'pid': is_valid_passport_id,
    'cid': is_valid_country_id
}


def is_valid_field(name, value):
    return validation_methods[name](value)


def main():
    expected = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid = 0

    for passport in read_passports():
        valid_fields = 0
        for field in passport:
            print(field)
            name, value = [i.strip() for i in field.split(":")]
            if name in expected and is_valid_field(name, value):
                valid_fields += 1
        if valid_fields == 7:
            valid += 1
            print(f'valid!')
        else:
            print(f'invalid!')

        print()

    print(f'Total valid passports: {valid}')

main()
