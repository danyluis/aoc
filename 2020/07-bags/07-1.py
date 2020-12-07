#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/7

import sys
import re
from collections import defaultdict
from collections import namedtuple

bag = namedtuple("bag", ("color", "number"))

color_description_re = re.compile('(\\d+) (\\w+ \\w+) bags?')
non_empty_bag_re = re.compile("^((\\w+ ){2})bags contain(.+)\\.")
empty_bag_re = re.compile('^((\\w+ ){2})bags contain no other bags\\.')


def load_graph():
    graph = defaultdict(set)

    for line in sys.stdin:
        line = line.strip()
        if empty_bag_re.match(line):
            color, foo = empty_bag_re.findall(line)[0]
        elif non_empty_bag_re.match(line):
            color, foo, included = non_empty_bag_re.findall(line)[0]
            color = color.strip()

            for part in included.split(','):
                number, included_color = color_description_re.findall(part)[0]

                number = int(number)
                included_color = included_color.strip()

                graph[color].add(bag(included_color, number))
    return graph


def can_get_from_to(start, end, graph):
    to_do = set(list(graph[start]))
    while to_do:
        color, foo = to_do.pop()
        if color == end:
            return True
        to_do |= graph[color]
    return False


graph = load_graph()
containing_shiny_gold = sum([1 for color in set(graph.keys()) if can_get_from_to(color, 'shiny gold', graph)])
print(f'Bag colors with shiny gold inside: {containing_shiny_gold}')

