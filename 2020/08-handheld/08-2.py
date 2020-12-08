#!/usr/bin/env python

# Advent of Code 2020
# https://adventofcode.com/2020/day/8

import sys

from collections import namedtuple
from collections import defaultdict

operation = namedtuple("operation", ("position", "op", "value"))

class Context(object):
    def __init__(self):
        self.pc = 0
        self.register = 0

def acc(value, context):
    context.register += value
    context.pc += 1

def jmp(value, context):
    context.pc += value

def nop(value, context):
    context.pc += 1

def load_program():
    name_to_f = {
        "acc" : acc,
        "jmp" : jmp,
        "nop" : nop
    }
    lines = enumerate(line.strip().split(" ") for line in sys.stdin)
    return [operation(position, name_to_f[line[0]], int(line[1])) for position, line in lines]

def does_it_finish(program):
    context = Context()
    times_run = defaultdict(int)
    while 0 <= context.pc < len(program):
        position, op, value = program[context.pc]
        if times_run[position] == 1:
            return (False, context.register)
        op(value, context)
        times_run[position] += 1
    return (True, context.register)

def main():
    program = load_program()

    changes = {
        jmp: nop,
        nop: jmp
    }

    for position, op, value in (line for line in program if line.op in (jmp, nop)):
        program[position] = operation(position, changes[op], value)
        finished, register = does_it_finish(program)

        if finished:
            print(f'Changed {op.__name__} in {position} to {changes[op].__name__}')
            print(f'Accumulator value is {register}')
            break

        program[position] = operation(position, op, value)

main()
