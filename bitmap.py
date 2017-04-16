#!/usr/bin/env python3

"""Search 2D bitmaps for blocks of adjacent cells whose values are 1"""

import numpy as np

from collections import deque

def adjacents(bitmap, cell, diagonals=False):
    """Generate all cells adjacent to the given cell (including itself)"""
    if not (0, 0) <= cell < bitmap.shape:
        return []
    i, j = cell
    rows, cols = bitmap.shape
    north = (i-1,j) if 0 < i else None
    east = (i,j+1) if j < cols - 1 else None
    south = (i+1,j) if i < rows - 1 else None
    west = (i,j-1) if 0 < j else None
    cells = [
        cell,
        north,
        east,
        south,
        west
    ]
    if diagonals:
        northeast = (i-1,j+1) if 0 < i and j < cols - 1 else None
        southeast = (i+1,j+1) if i < rows - 1 and j < cols - 1 else None
        southwest = (i+1,j-1) if i < rows - 1 and 0 < j else None
        northwest = (i-1,j-1) if 0 < i and 0 < j else None
        cells = [
            cell, 
            north, northeast, east, southeast,
            south, southwest, west, northwest
        ]
    return [c for c in cells if c is not None]

def explore(bitmap, cell, block=[], explored=set(), diagonals=False):
    """Recursively explore a block of adjacent bits whose values are 1"""
    for adjacent in adjacents(bitmap, cell, diagonals):
        if adjacent not in explored:
            explored.add(adjacent)
            if bitmap[adjacent]:
                block.append(adjacent)
                explore(bitmap, adjacent, block, explored, diagonals)
    return block

def blocks_recursive(bitmap, diagonals=False):
    """Generate all blocks of adjacent cells whose value is 1 recursively"""
    explored = set()
    for i, row in enumerate(bitmap):
        for j, col in enumerate(row):
            cell = i, j
            if bitmap[cell]:
                block = explore(
                    bitmap, cell,
                    block=[],
                    explored=explored,
                    diagonals=diagonals
                )
                if block:
                    yield sorted(block)

def blocks_que(bitmap, diagonals=False):
    """Generate all blocks of adjacent cells whose value is 1 via a deque"""
    explored = set()
    for i, row in enumerate(bitmap):
        for j, col in enumerate(row):
            cell = i, j
            block = deque()
            if bitmap[cell] and cell not in explored:
                block.append(cell)
                while not all(((c in explored) for c in block)):
                    cell = block.popleft()
                    explored.add(cell)
                    for adjacent in adjacents(bitmap, cell, diagonals):
                        if bitmap[adjacent] and adjacent not in set(block):
                            block.append(adjacent)
            explored.add(cell)
            if block:
                yield sorted(set(block))

def blocks(bitmap, strategy, **kwargs):
    """Generate all blocks using the given strategy"""
    return strategy(bitmap, **kwargs)

def show(bitmap, strategy, **kwargs):
    """Pretty-print a bitmap and all blocks of adjacent 1s in the bitmap"""
    print('bitmap:')
    print(*(''.join(map(str, row)) for row in bitmap), sep='\n')
    print('blocks:')
    for block in blocks(bitmap, strategy, **kwargs):
        print(block)

def load(string, col_sep=None, row_sep='\n'):
    """Load a bitmap as a numpy array from a string
    
    load('0101\n0111\n0101') -> numpy.array([
        [0, 1, 0, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 1]
    ])
    
    """
    bitmap = []
    for row in string.rstrip().split(row_sep):
        row = [c for c in row] if col_sep is None else row.split(col_sep)
        row = list(map(int, row))
        bitmap.append(row)
    return np.array(bitmap, dtype=int)

if __name__ == '__main__':
    import argparse
    import sys
    STRATEGIES = {
        'recursive': blocks_recursive,
        'que': blocks_que
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
        choices=set(STRATEGIES.keys()),
        help='specify a strategy to use'
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
        row_sep=args.row_delimiter
    )
    show(bitmap, STRATEGIES[args.strategy], diagonals=args.count_diagonals)
