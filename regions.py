#!/usr/bin/env python3

"""Search 2D bitmaps for regions of adjacent cells whose values are 'empty'
(as opposed to values that are 'walls').

Input is read as a string from stdin.

"""

from collections import deque

import numpy as np

def adjacents(bitmap, cell, diagonals=False):
    """Generate all regions adjacent to the given region (including itself)"""
    if not (0, 0) <= cell < bitmap.shape:
        return []
    i, j = cell
    rows, cols = bitmap.shape
    north = (i - 1, j) if 0 < i else None
    east = (i, j + 1) if j < cols - 1 else None
    south = (i + 1, j) if i < rows - 1 else None
    west = (i, j-1) if 0 < j else None
    region = [
        cell,
        north,
        east,
        south,
        west
    ]
    if diagonals:
        northeast = (i - 1, j + 1) if 0 < i and j < cols - 1 else None
        southeast = (i + 1, j + 1) if i < rows - 1 and j < cols - 1 else None
        southwest = (i + 1, j - 1) if i < rows - 1 and 0 < j else None
        northwest = (i - 1, j - 1) if 0 < i and 0 < j else None
        region = [
            cell, 
            north, northeast, east, southeast,
            south, southwest, west, northwest
        ]
    return [c for c in region if c is not None]

def explore(bitmap, cell, region=[], explored=set(), diagonals=False):
    """Recursively explore a region of adjacent bits whose values are 1"""
    for adjacent in adjacents(bitmap, cell, diagonals):
        if adjacent not in explored:
            explored.add(adjacent)
            if bitmap[adjacent]:
                region.append(adjacent)
                explore(bitmap, adjacent, region, explored, diagonals)
    return region

def regions_recursive(bitmap, diagonals=False):
    """Generate all regions of adjacent cells whose value is 1 recursively"""
    explored = set()
    for i, row in enumerate(bitmap):
        for j, col in enumerate(row):
            cell = i, j
            if bitmap[cell]:
                region = explore(
                    bitmap, cell,
                    region=[],
                    explored=explored,
                    diagonals=diagonals
                )
                if region:
                    yield sorted(region)

def regions_que(bitmap, diagonals=False):
    """Generate all regions of adjacent cells whose value is 1 via a deque"""
    explored = set()
    for i, row in enumerate(bitmap):
        for j, col in enumerate(row):
            cell = i, j
            region = deque()
            if bitmap[cell] and cell not in explored:
                region.append(cell)
                while not all(((c in explored) for c in region)):
                    cell = region.popleft()
                    explored.add(cell)
                    for adjacent in adjacents(bitmap, cell, diagonals):
                        if bitmap[adjacent] and adjacent not in set(region):
                            region.append(adjacent)
            explored.add(cell)
            if region:
                yield sorted(set(region))

def regions(bitmap, strategy, **kwargs):
    """Generate all regions using the given strategy"""
    return strategy(bitmap, **kwargs)

def show(bitmap, strategy, wall='#', empty='.', **kwargs):
    """Pretty-print a bitmap and all regions of adjacent 1s in the bitmap"""
    print(f'bitmap (empty="{empty}"; wall="{wall}"):')
    print(
        *(''.join([empty if c else wall for c in row]) for row in bitmap),
        sep='\n'
    )
    print('empty regions:')
    for region in regions(bitmap, strategy, **kwargs):
        print(region)

def load(s, col_sep=None, row_sep='\n', wall='#', empty='.'):
    """Load a bitmap as a numpy array from a string
    
    load('.#.#\n.###\n.#.#') -> numpy.array([
        [0, 1, 0, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 1]
    ])
    
    """
    bitmap = []
    for row in s.rstrip().split(row_sep):
        row = [c for c in row] if col_sep is None else row.split(col_sep)
        row = [int(c == empty) for c in row]
        bitmap.append(row)
    return np.array(bitmap, dtype=int)

if __name__ == '__main__':
    import argparse
    import sys
    STRATEGIES = {
        'recursive': regions_recursive,
        'que': regions_que
    }
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-c', '--column-delimiter',
        default=None,
        help='column delimiter string'
    )
    parser.add_argument(
        '-r', '--row-delimiter',
        default='\n',
        help='row delimiter string'
    )
    parser.add_argument(
        '-s', '--strategy',
        default='que',
        choices=STRATEGIES,
        help='specify a strategy to use'
    )
    parser.add_argument(
        '-w', '--wall',
        default='#',
        help="character to consider as a 'wall'",
    )
    parser.add_argument(
        '-e', '--empty',
        default='.',
        help="character to consider as 'empty'",
    )
    parser.add_argument(
        '-d', '--count-diagonals',
        action='store_true',
        help=(
            'consider diagonal cells to be adjacent; e.g., '
            '[0,0] and [1,1] would be considered adjacent'
        )
    )
    args = parser.parse_args()
    bitmap = load(
        sys.stdin.read(),
        col_sep=args.column_delimiter,
        row_sep=args.row_delimiter,
        wall=args.wall,
        empty=args.empty
    )
    show(
        bitmap,
        STRATEGIES[args.strategy],
        diagonals=args.count_diagonals,
        wall=args.wall,
        empty=args.empty
    )
