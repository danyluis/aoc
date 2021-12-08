#!/usr/bin/env python

import sys

def read_number(expr, i):
    end = i
    while end < len(expr) - 1 and expr[end + 1].isdigit():
        end += 1
    return end + 1, int(expr[i : end + 1])

def evaluate(expr, i):
    if expr[i] == '(':
        return evaluate(expr, i + 1)

    i, value = eval_number(expr, i)

    if expr[i] == '*':
        return value * evaluate(expr, i + 1)

    if expr[i] == '+':
        return value + evaluate(expr, i + 1)

    if expr[i] == ')':
        return value


def next_token(expr, i):
    if expr[i].isdigit():
        return read_number(expr, i)

    return i + 1, expr[i]

def is_oper(c):
    return c in {'*', '+'}

def eval(a, oper, b):
    if oper == '+':
        return int(a) + int(b)
    elif oper == '*':
        return int(a) * int(b)


from collections import deque

def operate(stack):
    print(stack)
    if len(stack) == 1:
        return stack

    if len(stack) >= 3:
        c = stack.pop()
        b = stack.pop()
        a = stack.pop()

        if a == '(' and c == ')':
            stack.append(b)
            operate(stack)
        elif is_oper(b):
            stack.append(eval(a, b, c))
            operate(stack)
        else:
            stack.append(a)
            stack.append(b)
            stack.append(c)

def evaluate(expr):
    print(expr)
    stack = deque()
    i = 0
    while i < len(expr):
        i, token = next_token(expr, i)

        print(stack)

        if is_oper(token):
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')' or i == len(expr):
            stack.append(token)
            operate(stack)
        else:
            stack.append(token)
            operate(stack)

    while len(stack) > 1:
        operate(stack)

    print(stack)
    print('\n\n')
    return stack.pop()



expressions = [
    line.strip().replace(" ", "")
    for line in sys.stdin.readlines() if line.strip()
]

results = list(map(lambda expr: evaluate(expr), expressions))
# print("\n\n".join(str(r) for r in results))
print(sum(results))