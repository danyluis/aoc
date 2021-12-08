#!/usr/bin/env python

import sys
import re
import math
import copy

from collections import defaultdict
from collections import namedtuple
from functools import reduce

title_re = re.compile('^Tile (\\d+):')

TOP, RIGHT, BOTTOM, LEFT = list(range(4))
SIDES = (TOP, RIGHT, BOTTOM, LEFT)

SolutionTile = namedtuple('SolutionTile', ('tile_id', 'rotation_id', 'rotation'))
TileRotation = namedtuple('TileRotation', ('tile_id', 'rotation_id'))

def opposite(side):
    return (side + 2) % len(SIDES)

def b_rotations_that_match(fixed_rotation, a_side, b_rotations):
    matching_rotations = set()

    for i, b_keys in enumerate(b_rotations):
        if b_keys[opposite(a_side)] == fixed_rotation[a_side]:
            matching_rotations.add(i)

    return matching_rotations

def bit_key(tile):
    height, width = len(tile), len(tile[0])
    k = (
        tile[0] +
        "".join([tile[i][width - 1] for i in range(height)]) +
        tile[height - 1][::-1] +
        "".join([tile[i][0] for i in range(height - 1, -1, -1)])
    )
    return "".join(str(i) for i in k)

def top(bit_key):
    tile_side = len(bit_key) // 4
    return bit_key[0 : tile_side]

def right(bit_key):
    tile_side = len(bit_key) // 4
    return bit_key[tile_side : 2 * tile_side]

def bottom(bit_key):
    tile_side = len(bit_key) // 4
    return bit_key[2 * tile_side : 3 * tile_side][::-1]

def left(bit_key):
    tile_side = len(bit_key) // 4
    return bit_key[3 * tile_side : 4 * tile_side][::-1]

def keys_from_bit_key(bit_key):
    keys = (
        top(bit_key),
        right(bit_key),
        bottom(bit_key),
        left(bit_key)
    )

    return keys

def rotate(bit_key, times):
    times = times % 4
    if not times:
        return bit_key[:]
    side = len(bit_key) // 4
    cut = len(bit_key) - times * side
    return bit_key[cut:] + bit_key[:cut]

def get_rotations(tile):
    bkey = bit_key(tile)
    rkey = bkey[::-1]

    keys = [None] * 8
    for i in range(4):
        keys[i] = keys_from_bit_key(rotate(bkey, i))

    for i in range(4, 8):
        keys[i] = keys_from_bit_key(rotate(rkey, i - 4))

    return tuple(keys)

def all_matches_on_side(fixed_tile_id, fixed_tile_rotation, side, tile_rotation_map, avoid_ids):
    matching = set()
    for tile_id, rotations in tile_rotation_map.items():
        if tile_id == fixed_tile_id or tile_id in avoid_ids:
            continue

        b_matching_rotations = b_rotations_that_match(fixed_tile_rotation, side, rotations)
        matching |= {TileRotation(tile_id, rotation_id) for rotation_id in b_matching_rotations}

    return matching

def get_all_rotations_from_tile_map(tile_map):
    return {n : get_rotations(tile) for n, tile in tile_map.items()}

def combinations(height, width):
    for i in range(height):
        for j in range(width):
            yield (i, j)

def solve_grid_rec(grid, index_list, curr_position, used_ids, tile_rotation_map):
    if curr_position >= len(index_list):
        return True

    i, j = index_list[curr_position]

    top_tile_id, top_tile_rotation_id, top_tile_rotation = None, None, None
    if i > 0:
        top_tile_id, top_tile_rotation_id, top_tile_rotation = grid[i - 1][j]

    left_tile_id, left_tile_rotation_id, left_tile_rotation = None, None, None
    if j > 0:
        left_tile_id, left_tile_rotation_id, left_tile_rotation = grid[i][j - 1]

    right_matchings = set()
    if left_tile_id is not None:
        right_matchings = all_matches_on_side(
            left_tile_id,
            left_tile_rotation,
            RIGHT,
            tile_rotation_map,
            used_ids)

    bottom_matchings = set()
    if top_tile_id is not None:
        bottom_matchings = all_matches_on_side(
            top_tile_id,
            top_tile_rotation,
            BOTTOM,
            tile_rotation_map,
            used_ids)

    selected_matchings = set()
    if right_matchings and not bottom_matchings:
        selected_matchings = right_matchings
    elif bottom_matchings and not right_matchings:
        selected_matchings = bottom_matchings
    else:
        selected_matchings = right_matchings & bottom_matchings

    if not selected_matchings:
        return False

    for next_tile_id, tile_rotation_id in selected_matchings:
        grid[i][j] = SolutionTile(next_tile_id, tile_rotation_id, tile_rotation_map[next_tile_id][tile_rotation_id])
        if solve_grid_rec(grid, index_list, curr_position + 1, used_ids | {next_tile_id}, tile_rotation_map):
            return True
        grid[i][j] = None

    return False

def solve_grid(tile_map):
    tile_rotation_map = get_all_rotations_from_tile_map(tile_map)

    GRID_SIZE = int(math.sqrt(len(tile_map)))
    solved_grid = [[None] * GRID_SIZE for i in range(GRID_SIZE)]

    grid_index_list = list(combinations(GRID_SIZE, GRID_SIZE))
    for tile_id, rotations in tile_rotation_map.items():
        for rotation_id, rotation in enumerate(rotations):
            solved_grid[0][0] = SolutionTile(tile_id, rotation_id, rotation)
            if solve_grid_rec(solved_grid, grid_index_list, 1, {tile_id}, tile_rotation_map):
                return solved_grid

    return None

def read_tile_map():
    tile_map = {}
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        number = title_re.findall(line)[0]

        tile = []
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            tile.append(line)

        tile_map[int(number)] = tile

    return tile_map

def part_a(solved_grid):
    sol_tiles = [
        solved_grid[0][0],
        solved_grid[0][-1],
        solved_grid[-1][0],
        solved_grid[-1][-1]
    ]
    print(f'Part A: {reduce(lambda a, b: a * b, (sol.tile_id for sol in sol_tiles))}')

def rotate_matrix(m, times):
    times = times % 4
    r = m
    for i in range(times):
        r = list(map(list, zip(*r[::-1])))
    return r

def vflip(m):
    return m[::-1]


def apply_rotation(m, rotation_id):
    if rotation_id in range(4): # STRAIGHT ROTATIONS
        return rotate_matrix(m, rotation_id)

    r = rotate_matrix(vflip(m), 1) # FLIPPED ROTATIONS
    return rotate_matrix(r, rotation_id - 4)

def test_rotations():
    a = [[1,2,3],[4,5,6],[7,8,9]]
    bk = bit_key(a)
    assert bk == "123369987741"

    rotations = get_rotations(a)
    print(rotations)

    for rotation_id in range(8):
        r = apply_rotation(a, rotation_id)
        print(r)
        print(keys_from_bit_key(bit_key(r)))

def shave_tile(tile):
    return [ [tile[i][j] for j in range(1, len(tile[0]) - 1)] for i in range(1, len(tile) - 1)]

def test_shave():
    a = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]
    print(f'tile={a}, shaved={shave_tile(a)}')


def copy_tile_to_chart(tile, chart, row, col):
    for i in range(len(tile)):
        for j in range(len(tile[0])):
            chart[i + row][j + col] = tile[i][j]

def get_col(chart, col):
    return tuple(chart[i][col] for i in range(len(chart)))

def get_row(chart, row):
    return tuple(chart[row])

def build_map(solved_grid, tile_map):
    b = copy.deepcopy(solved_grid)
    height, width = len(b), len(b[0])
    for row in range(height):
        for col in range(width):
            tile_id, rotation_id, foo = b[row][col]
            b[row][col] = shave_tile(apply_rotation(tile_map[tile_id], rotation_id))

    tile_height, tile_width = len(b[0][0]), len(b[0][0][0])
    chart_height = height * tile_height
    chart_width = width * tile_width

    chart = [[0] * chart_width for i in range(chart_height)]

    for row in range(height):
        for col in range(width):
            copy_tile_to_chart(b[row][col], chart, row * tile_height, col * tile_width)
    return chart

def monster_indexes():
    monster = ['                  #', '#    ##    ##    ###', ' #  #  #  #  #  #']
    for i, line in enumerate(monster):
        for j, c in enumerate(line):
            if c == '#':
                yield (i, j)

def mark_monster(chart, row, col):
    for i, j in monster_indexes():
        if i + row >= len(chart) or j + col >= len(chart[0]):
            return False
        if chart[row + i][col + j] != '#':
            return False

    for i, j in monster_indexes():
        chart[row + i][col + j] = '.'

    return True

def part_b(chart):
    for rotation_id in range(8):
        rotated = apply_rotation(chart, rotation_id)
        marked = False
        for row in range(len(rotated)):
            for col in range(len(rotated[0])):
                if mark_monster(rotated, row, col): # Don't short-circuit
                    marked = True
        if marked:
            wave_count = sum(sum(map(lambda c: 1 if c == '#' else 0, rotated[i])) for i in range(len(rotated)))
            print(f'Part B: For rotation {rotation_id}, #waves is: {wave_count}')

tile_map = read_tile_map()

solved_grid = solve_grid(tile_map)
part_a(solved_grid)

chart = build_map(solved_grid, tile_map)
part_b(chart)