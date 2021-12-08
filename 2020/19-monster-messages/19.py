#!/usr/bin/env python

import sys
import regex

message_re = regex.compile('[ab]+')
rule_re = regex.compile('^(\\d+): (.+)')

def expand_value(value, grammar):
    if type(value) is str:
        return value
    else:
        return "(" + expand(value, grammar) + ")"

def expand(i, grammar):
    prods = grammar[i]
    parts = []
    for prod in prods:
        str_part = ""
        for value in prod:
            str_part += expand_value(value, grammar)
        parts.append(str_part)
    return "|".join(parts)

def generate_re_part_1(grammar):
    return expand(0, grammar)

def generate_re_part_2(grammar):
    _42 = expand(42, grammar)
    _31 = expand(31, grammar)
    return f'({_42})+(?P<sec>({_42})(?&sec)?({_31}))'

def count_using_re(messages, grammar_re):
    match_count = 0
    for message in messages:
        matches = grammar_re.fullmatch(message) is not None
        match_count += int(matches)
    return match_count

def fix(s):
    if s is None:
        return None
    if s.isnumeric():
        return int(s.strip())
    return s.replace('\"', '')

messages = set()
grammar = {}

for line in (line.strip() for line in sys.stdin.readlines() if line.strip()):
    if message_re.match(line):
        messages.add(line)
    else:
        istr, rest = line.split(':')
        i = int(istr)

        prods = []
        parts = rest.split('|')
        for part in parts:
            values = []
            for rule in (p.strip() for p in part.strip().split(" ")):
                if rule.isnumeric():
                    values.append(int(rule))
                else:
                    values.append(rule.replace("\"", ""))
            prods.append(values)

        grammar[i] = prods

grammar_re_str_1 = generate_re_part_1(grammar)
grammar_re_1 = regex.compile(grammar_re_str_1)
count_1 = count_using_re(messages, grammar_re_1)

grammar_re_str_2 = generate_re_part_2(grammar)
grammar_re_2 = regex.compile(grammar_re_str_2)
count_2 = count_using_re(messages, grammar_re_2)

print(f'Part one: {count_1}')
print(f'Part two: {count_2}')
