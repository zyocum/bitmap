# bitmap
Search 2D bitmaps for blocks of adjacent cells whose values are 1

## Usage
	./bitmap.py -h
	usage: bitmap.py [-h] [-c COLUMN_DELIMITER] [-r ROW_DELIMITER]
	                 [-s {recursive,que}] [-d]
	
	Search 2D bitmaps for blocks of adjacent cells whose values are 1
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -c COLUMN_DELIMITER, --column-delimiter COLUMN_DELIMITER
	                        column delimiter string (default: None)
	  -r ROW_DELIMITER, --row-delimiter ROW_DELIMITER
	                        row delimiter string (default: )
	  -s {recursive,que}, --strategy {recursive,que}
	                        specify a strategy to use (default: que)
	  -d, --count-diagonals
	                        consider diagonal cells to be adjacent; e.g., [0,0]
	                        and [1,1] would be considered adjacent (default:
	                        False)
## Examples
	$ echo "0101
	0111
	0101" > bitmap.txt
	$ ./bitmap.py < bitmap.txt 
	bitmap:
	0101
	0111
	0101
	blocks:
	[(0, 1), (0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 3)]  

There are two strategies that can be set via the `-s/--strategy` option:

1. `que`: This strategy models each block as a double-ended que, popping and pushing cells from the que until each block has been exhaustively explored.
2. `recursive`: This strategy explores blocks using recursive method calls.  This strategy is limited by the call-stack size (blocks larger than the call-stack size in the input will cause a stack overflow).

There are several sample files in the `bitmaps` directory:

	$ for f in bitmaps/*.txt; do
		./bitmap.py < "$f"
	done
	bitmap:
	10
	00
	blocks:
	[(0, 0)]
	bitmap:
	00
	01
	blocks:
	[(1, 1)]
	bitmap:
	00000
	01100
	01100
	00000
	00001
	blocks:
	[(1, 1), (1, 2), (2, 1), (2, 2)]
	[(4, 4)]
	bitmap:
	10001
	01101
	01101
	00001
	00001
	blocks:
	[(0, 0)]
	[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
	[(1, 1), (1, 2), (2, 1), (2, 2)]
	bitmap:
	0101
	0111
	0101
	blocks:
	[(0, 1), (0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 3)]
	bitmap:
	0011111100
	0100000010
	0101001010
	0101001010
	0100000010
	0101001010
	0100110010
	0100000010
	0011111100
	blocks:
	[(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
	[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
	[(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8)]
	[(2, 3), (3, 3)]
	[(2, 6), (3, 6)]
	[(5, 3)]
	[(5, 6)]
	[(6, 4), (6, 5)]
	[(8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)]


You can supply the `-d/--count-diagonals` option if you want to include diagonal cells as adjacent to one another:

	$ for f in bitmaps/*.txt; do
		./bitmap.py < "$f"
	bitmap:
	10
	00
	blocks:
	[(0, 0)]
	bitmap:
	00
	01
	blocks:
	[(1, 1)]
	bitmap:
	00000
	01100
	01100
	00000
	00001
	blocks:
	[(1, 1), (1, 2), (2, 1), (2, 2)]
	[(4, 4)]
	bitmap:
	10001
	01101
	01101
	00001
	00001
	blocks:
	[(0, 0), (1, 1), (1, 2), (2, 1), (2, 2)]
	[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
	bitmap:
	0101
	0111
	0101
	blocks:
	[(0, 1), (0, 3), (1, 1), (1, 2), (1, 3), (2, 1), (2, 3)]
	bitmap:
	0011111100
	0100000010
	0101001010
	0101001010
	0100000010
	0101001010
	0100110010
	0100000010
	0011111100
	blocks:
	[(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 1), (1, 8), (2, 1), (2, 8), (3, 1), (3, 8), (4, 1), (4, 8), (5, 1), (5, 8), (6, 1), (6, 8), (7, 1), (7, 8), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)]
	[(2, 3), (3, 3)]
	[(2, 6), (3, 6)]
	[(5, 3), (5, 6), (6, 4), (6, 5)]
