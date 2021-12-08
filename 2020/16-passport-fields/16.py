#!/usr/bin/env python

import sys
import re
from collections import namedtuple

rule_re = re.compile("([ \\w]+): (\\d+)-(\\d+) or (\\d+)-(\\d+)")
Rule = namedtuple("Rule", ("name", "a", "b", "c", "d"))

my_ticket = (83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71)

def satisfies_rule(value, rule):
    return rule.a <= value <= rule.b or rule.c <= value <= rule.d

def get_invalid_values(values, rules):
    invalid = set()
    for value in values:
        for rule in rules:
            if satisfies_rule(value, rule):
                break;
        else:
            invalid.add(value)
    return invalid

def new_rule(name, stra, strb, strc, strd):
    return Rule(name, int(stra), int(strb), int(strc), int(strd))

def get_rules():
    fields =[
        "departure location: 27-840 or 860-957",
        "departure station: 28-176 or 183-949",
        "departure platform: 44-270 or 277-967",
        "departure track: 33-197 or 203-957",
        "departure date: 47-660 or 677-955",
        "departure time: 45-744 or 758-971",
        "arrival location: 42-636 or 642-962",
        "arrival station: 44-243 or 252-962",
        "arrival platform: 46-428 or 449-949",
        "arrival track: 25-862 or 876-951",
        "class: 26-579 or 585-963",
        "duration: 38-683 or 701-949",
        "price: 41-453 or 460-970",
        "route: 48-279 or 292-963",
        "row: 33-617 or 637-955",
        "seat: 39-328 or 351-970",
        "train: 35-251 or 264-957",
        "type: 25-380 or 389-951",
        "wagon: 42-461 or 480-965",
        "zone: 33-768 or 789-954"
    ]
    return {
        name : new_rule(name, a, b, c, d)
        for name, a, b, c, d in [rule_re.findall(f)[0] for f in fields]
    }

def get_valid_tickets(rules, tickets):
    error_rate = 0
    valid_tickets = set()
    for ticket in tickets:
        invalid_values = get_invalid_values(ticket, rules.values())
        if not invalid_values:
            valid_tickets.add(ticket)
        error_rate += sum(invalid_values)
    return error_rate, valid_tickets

def part_one(rules, tickets):
    error_rate, foo = get_valid_tickets(rules, tickets)
    print(f'Part1: error_rate={error_rate}')

def part_two(rules, tickets, my_ticket):
    position_rules = [set(rules.values())] * len(my_ticket)

    foo, valid_tickets = get_valid_tickets(rules, tickets)
    valid_tickets |= {my_ticket}

    for i in range(len(my_ticket)):
        curr_rules = position_rules[i]
        curr_valid = set()
        for rule in curr_rules:
            if all(satisfies_rule(value, rule) for value in [ticket[i] for ticket in valid_tickets]):
                curr_valid.add(rule)
        position_rules[i] = curr_valid

    while True:
        lengths = tuple(len(rules) for rules in position_rules)
        for i in range(len(position_rules)):
            rules_i = position_rules[i]
            if len(rules_i) == 1:
                for j in range(len(position_rules)):
                    if j == i or len(position_rules[j]) == 1:
                        continue
                    new_set = position_rules[j] - rules_i
                    position_rules[j] = new_set
        lengths = tuple(len(rules) for rules in position_rules)
        if all(length==1 for length in lengths):
            break

    print(f'\nPart 2:\nRules:')
    selected_rules = [rule_set.pop() for rule_set in position_rules]
    for i, rule in enumerate(selected_rules):
        print(f'{i}: {rule}')

    mult = 1
    for i, rule in enumerate(selected_rules):
        if rule.name.startswith("departure"):
            mult *= my_ticket[i]
    print(f'Multiplied departure values = {mult}')


def read_tickets():
    tickets = []
    for line in (line.strip() for line in sys.stdin.readlines() if line.strip()):
        tickets.append(tuple(int(n) for n in line.split(',')))
    return tickets

rules = get_rules()
tickets = read_tickets()

part_one(rules, tickets)
part_two(rules, tickets, my_ticket)

