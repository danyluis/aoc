#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/12

import sys
from collections import defaultdict
from collections import Counter

START, END = 'start', 'end'
graph = defaultdict(list)

def can_visit_1(cave, graph, visited):
    return cave.isupper() or visited[cave] == 0

def can_visit_2(cave, graph, visited):
    if cave.isupper():
        return True

    if cave in (START, END):
        return visited[cave] == 0

    if cave.islower():
        if all(visited[c] < 2 for c in visited if c.islower()):
            return True
        else:
            return visited[cave] == 0

def count_paths(cave, graph, visited, f_can_visit):
    if cave == END:
        return 1
    return sum(count_paths(nxt, graph, visited + Counter({nxt}), f_can_visit)
        for nxt in graph[cave] if f_can_visit(nxt, graph, visited))

for a, b in [line.strip().split('-') for line in sys.stdin.readlines()]:
    graph[a].append(b)
    graph[b].append(a)

print(f'part 1: {count_paths(START, graph, Counter([START]), can_visit_1)}')
print(f'part 2: {count_paths(START, graph, Counter([START]), can_visit_2)}')

