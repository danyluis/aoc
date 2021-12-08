#!/usr/bin/env python

import sys
from collections import deque

def read_decks():
    sys.stdin.readline()
    deck1, deck2 = [], []
    curr = deck1
    while True:
        line = sys.stdin.readline().strip()
        if line.startswith('P'):
            continue
        if not line:
            if curr is deck1:
                curr = deck2
                continue
            else:
                break
        curr.append(int(line))
    return (deck1, deck2)

def score(deck):
    score = 0
    for i, card in enumerate(deck):
        score += (len(deck) - i) * card
    return score

def part_a(deck1, deck2):
    total_len = len(deck1) + len(deck2)
    deck1, deck2 = deque(deck1), deque(deck2)
    while len(deck1) > 0 and len(deck2) > 0:
        a, b = deck1.popleft(), deck2.popleft()
        mx, mn = max(a, b), min(a, b)
        if a == mx:
            deck1.append(mx)
            deck1.append(mn)
        else:
            deck2.append(mx)
            deck2.append(mn)

    print(f'deck1={deck1}')
    print(f'deck2={deck2}\n')
    winning = deck1 if len(deck1) else deck2
    print(f'Winning score: {score(winning)}')

deck1, deck2 = read_decks()
part_a(deck1, deck2)