#!/usr/bin/env python

# Advent of Code 2015
# https://adventofcode.com/2015/day/5

import sys
import re

def switch(board, top_row, left_col, bottom_row, right_col, f):
    for i in range(top_row, bottom_row + 1):
        for j in range(left_col, right_col + 1):
            board[i][j] = f(board[i][j])


def execute_on_board(instructions, board, function_table):
    instruction_re = re.compile("((\\w+)( \\w+)?) (\\d+),(\\d+) through (\\d+),(\\d+)")

    for line in instructions:
        match = instruction_re.findall(line)[0]
        start_text = match[0]
        top_row, left_col, bottom_row, right_col = (int(s) for s in match[3:])
        switch(board, top_row, left_col, bottom_row, right_col, function_table[start_text])

    brightness = sum(sum(board[row]) for row in range(len(board)))
    return board


instructions = [line.strip() for line in sys.stdin.readlines() if line.strip()]

board = execute_on_board(
    instructions,
    [[False] * 1000 for i in range(1000)],
    {"turn on" : lambda a: True, "turn off" : lambda a: False, "toggle" : lambda a: not a}
)
print(f'Number of lights on: {sum(sum(board[row]) for row in range(len(board)))}')

board = execute_on_board(
    instructions,
    [[0] * 1000 for i in range(1000)],
    {"turn on" : lambda a: a + 1, "turn off" : lambda a: max(0, a - 1), "toggle" : lambda a: a + 2}
)
print(f'Total brightness: {sum(sum(board[row]) for row in range(len(board)))}')
