#!/usr/bin/env python

# Advent of Code 2021
# https://adventofcode.com/2021/day/4

import sys

class Bingo:

    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.selected = [[False] * self.width for i in range(self.height)]

    def select(self, number):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == number:
                    self.selected[row][col] = True

    def is_bingo(self):
        for row in range(self.height):
            if all(self.selected[row]):
                return True

        for col in range(self.width):
            if all([self.selected[row][col] for row in range(self.height)]):
                return True

        return False

    def sum_non_selected(self):
        s = 0
        for row in range(self.height):
            for col in range(self.width):
                if not self.selected[row][col]:
                    s += self.board[row][col]
        return s

    def __repr__(self):
        return str(self.board) + "\n" + str(self.selected)


def get_row(line):
    return [int(s) for s in line.strip().split(' ') if s]


def main():
    bingos = set()
    numbers = [int(s) for s in sys.stdin.readline().strip().split(',') if s]
    print(f'numbers: {numbers}')

    SIZE = 5

    line = sys.stdin.readline();
    while line:
        board = []
        for i in range(SIZE):
            line = sys.stdin.readline().strip()
            board.append(get_row(line))
        
        bingo = Bingo(board)
        bingos.add(bingo)
        line = sys.stdin.readline()

    found = False

    i = 0
    while i < len(numbers):
        for bingo in bingos:
            bingo.select(numbers[i])
        i += 1

        bingoed = set([bingo for bingo in bingos if bingo.is_bingo()])
        bingos -= bingoed

        if len(bingos) == 1:
            break            

    last_bingo = bingos.pop()
    while not last_bingo.is_bingo():
        last_bingo.select(numbers[i])
        i += 1

    s = last_bingo.sum_non_selected()
    n = numbers[i - 1]
    print(f'Board: {bingo}')
    print(f'sum_non_selected: {s}')
    print(f'number: {n}')
    print(f'result = {s * n}')
    
main()

