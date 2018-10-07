# bitmap
Search 2D bitmaps for regions of adjacent cells whose values are 'empty' (as
opposed to values that are 'walls'). Input is read as a string from stdin.

## Usage
    $ ./regions.py -h                                                                      
    usage: regions.py [-h] [-c COLUMN_DELIMITER] [-r ROW_DELIMITER]
                      [-s {recursive,que}] [-w WALL] [-e EMPTY] [-d]

    Search 2D bitmaps for regions of adjacent cells whose values are 'empty' (as
    opposed to values that are 'walls'). Input is read as a string from stdin.

    optional arguments:
      -h, --help            show this help message and exit
      -c COLUMN_DELIMITER, --column-delimiter COLUMN_DELIMITER
                            column delimiter string (default: None)
      -r ROW_DELIMITER, --row-delimiter ROW_DELIMITER
                            row delimiter string (default: )
      -s {recursive,que}, --strategy {recursive,que}
                            specify a strategy to use (default: que)
      -w WALL, --wall WALL  character to consider as a 'wall' (default: #)
      -e EMPTY, --empty EMPTY
                            character to consider as 'empty' (default: .)
      -d, --count-diagonals
                            consider diagonal cells to be adjacent; e.g., [0,0]
                            and [1,1] would be considered adjacent (default:
                            False)
## Examples
    $ echo ".#.#
    .###
    .#.#" > bitmap.txt
    $ ./regions.py < bitmap.txt 
    bitmap (empty="."; wall="#"):
    .#.#
    .###
    .#.#
    empty regions:
    [(0, 0), (1, 0), (2, 0)]
    [(0, 2)]
    [(2, 2)]


There are two strategies that can be set via the `-s/--strategy` option:

1. `que`: This strategy models each region as a double-ended que, popping and pushing cells from the que until each region has been exhaustively explored.
2. `recursive`: This strategy explores regions using recursive method calls.  This strategy is limited by the call-stack size (regions larger than the call-stack size in the input will cause a stack overflow).

There are several sample files in the `bitmaps` directory:

    for f in bitmaps/*.txt; do
        ./regions.py < "$f"
    done
    bitmap (empty="."; wall="#"):
    #.
    ..
    empty regions:
    [(0, 1), (1, 0), (1, 1)]
    bitmap (empty="."; wall="#"):
    ..
    .#
    empty regions:
    [(0, 0), (0, 1), (1, 0)]

    bitmap (empty="."; wall="#"):
    .....
    .##..
    .##..
    .....
    ....#
    empty regions:
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 3), (1, 4), (2, 0), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3)]
    bitmap (empty="."; wall="#"):
    #...#
    .##.#
    .##.#
    ....#
    ....#
    empty regions:
    [(0, 1), (0, 2), (0, 3), (1, 0), (1, 3), (2, 0), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
    bitmap (empty="."; wall="#"):
    .#.#
    .###
    .#.#
    empty regions:
    [(0, 0), (1, 0), (2, 0)]
    [(0, 2)]
    [(2, 2)]
    bitmap (empty="."; wall="#"):
    ..######..
    .#......#.
    .#.#..#.#.
    .#.#..#.#.
    .#......#.
    .#.#..#.#.
    .#..##..#.
    .#......#.
    ..######..
    empty regions:
    [(0, 0), (0, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1)]
    [(0, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 8), (8, 9)]
    [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 2), (2, 4), (2, 5), (2, 7), (3, 2), (3, 4), (3, 5), (3, 7), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (5, 4), (5, 5), (5, 7), (6, 2), (6, 3), (6, 6), (6, 7), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
