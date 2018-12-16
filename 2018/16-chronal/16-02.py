# Advent of Code 2018
# https://adventofcode.com/2018/day/16
# Dany Farina (danyluis@gmail.com)

from sys import *
from operator import itemgetter
from collections import *
from itertools import *
from re import *

registers = [0] * 4

gteq      = set(('gt', 'eq'))    
twosuffix = ('ir', 'ri', 'rr')
onesuffix = ('i', 'r')

getval = {
    "r": lambda a: registers[a],
    "i": lambda a: a
}

ops = {
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "ban": lambda a, b: a & b,
    "bor": lambda a, b: a | b,
    "set": lambda a, b: a,
    "gt" : lambda a, b: 1 if a > b else 0,
    "eq" : lambda a, b: 1 if a == b else 0
}

def oplist():
    return (a + b for a in ops.keys() for b in (twosuffix if a in gteq else onesuffix))

opToName = { i : set(oplist()) for i in range(16) }

def compute(op, a, b):
    if op[:2] in gteq:
        prefix = op[:2]
        suffix = op[2:]
        return ops[prefix]( getval[suffix[0]](a), getval[suffix[1]](b) )
    else:
        suffix = op[-1:]
        prefix = op[:-1]
        if prefix == 'set':
            ret = ops[prefix]( getval[suffix[0]](a), 0 )
        else:
            ret = ops[prefix]( getval['r'](a), getval[suffix[0]](b) )

    return ret

def apply( op, a, b, c ):
    registers[c] = compute(op, a, b)

def ria(s):
    return [int(s) for s in s.strip().split(' ')]

def countSameResult(before, inst, after):
    global registers, opToName

    a, b, c = inst[1:]
    same = 0

    names = set()
    for op in oplist():
        registers = before[:]
        apply( op, a, b, c )

        if registers == after:
            names.add(op)
            same += 1

    if names:
        opToName[inst[0]] &= names

    return same

def printdict(d, name):
    print name
    for k in d.keys():
        print "{} => {}".format(k, sorted(list(d[k])))
    print

def validPerm(codeToName, opToName):
    for code, name in codeToName:
        if name not in opToName[code]:
            return False
    return True

def main():
    reState = compile("^\\w+:\\s+\\[(\\d+), (\\d+), (\\d+), (\\d+)]")
    global registers, opToName

    countSame = 0
    while True:
        before = [int(i) for i in reState.split(stdin.readline().strip()) if len(i)]
        if not before:
            break
        inst = ria(stdin.readline())
        after = [int(i) for i in reState.split(stdin.readline().strip()) if len(i)]
        stdin.readline()
        same = countSameResult( before, inst, after )
        countSame += 1 if same >= 3 else 0

    print "countSame = {}".format(countSame)

    done = {}
    while opToName:

        for op, names in opToName.iteritems():
            if len(names) == 1:
                done[op] = names

        opToName = {
            op : reduce( lambda s1, s2: s1 - s2, done.values(), opToName[op] ) 
            for op in opToName.keys() if opToName[op]
        }

    printdict(done, "codes to names")
    names = [done[i].pop() for i in range(16)]

    registers = [0] * 4
    line = stdin.readline().strip()
    while not line:
        line = stdin.readline().strip()

    while line:
        inst = ria(line.strip())
        apply( names[inst[0]], *(inst[1:]) )
        line = stdin.readline().strip()

    print registers
    print registers[0]

main()
