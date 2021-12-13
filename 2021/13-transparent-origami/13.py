#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/13

import sys

def print_paper(paper, title=''):
    if title:
        print(title)
    for r in range(len(paper)):
        for c in range(len(paper[r])):
            print('#' if paper[r][c] else ' ', end='')
        print()
    print()

def all_cells(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            yield (r, c,)

def sub(matrix, r1, c1, r2, c2):
    ret = [[0] * (c2 - c1 + 1) for r in range(r2 - r1 + 1)]
    for r, c in all_cells(ret):
        ret[r][c] = matrix[r + r1][c + c1]
    return ret

def flip_left(matrix):
    return [row[::-1] for row in matrix]

def add_matrix(m1, m2):
    big, small = m2, m1
    if len(m1[0]) > len(m2[0]):
        big, small = m1, m2

    ret = sub(big, 0, 0, len(big) - 1, len(big[0]) - 1)
    diff = len(big[0]) - len(small[0])
    for r in range(len(big)):
        for c in range(len(big[0])):
            ret[r][c + diff] = ret[r][c + diff] or small[r][c]
    return ret

def fold_up(matrix, r):
    upper = sub(matrix, 0, 0, r - 1, len(matrix[0]) - 1)
    lower = sub(matrix, r + 1, 0, len(matrix) - 1, len(matrix[0]) - 1)[::-1]
    return add_matrix(upper, lower)

def fold_left(matrix, c):
    left  = sub(matrix, 0, 0, len(matrix) - 1, c - 1)
    right = flip_left(sub(matrix, 0, c + 1, len(matrix) - 1, len(matrix[0]) - 1))
    return add_matrix(left, right)

def fold(matrix, fold_rc):
    r, c = fold_rc
    return fold_up(matrix, r) if r else fold_left(matrix, c)

def read_paper():
    points, maxr, maxc = [], 0, 0
    while True:
        line = sys.stdin.readline().strip()
        if not line: break
        c, r = [int(s.strip()) for s in line.strip().split(',')]
        maxr, maxc = max(maxr, r), max(maxc, c)
        points.append((r, c,))

    paper = [[False] * (maxc + 1) for r in range(maxr + 1)]
    for r, c in points:
        paper[r][c] = True
    return paper

def read_folds():
    folds = []
    while True:
        line = sys.stdin.readline()
        if not line: break
        pref, suff = line.split('=')
        folds.append((int(suff), 0,) if pref[-1] == 'y' else (0, int(suff),))
    return folds

paper = read_paper()
folds = read_folds()

folded = paper
for r, c in folds:
    folded = fold_up(folded, r) if r else fold_left(folded, c)
    print(len(list(folded[r][c] for r, c in all_cells(folded) if folded[r][c])))

print_paper(folded, 'code:')

