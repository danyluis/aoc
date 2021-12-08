#!/usr/bin/env python

import sys
import re

food_re = re.compile('(^(\\w+ )+)\\(contains ((\\w+)(, \\w+)*)\\)')

for line in [line.strip()  for line in sys.stdin.readlines() if line.strip()]:
    ingredients, foo, allergens, bar, foobar = food_re.findall(line)[0]
    ingredients = ingredients.strip().split(" ")
    allergens = allergens.strip().split(", ")
    print(ingredients)
    print(allergens)