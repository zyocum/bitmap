# bitmap
Search 2D bitmaps for blocks of adjacent cells whose values are 1

##Usage
	./bitmap.py -h
	usage: bitmap.py [-h] [-c COLUMN_DELIMITER] [-r ROW_DELIMITER] [-d]
	
	Search 2D bitmaps for blocks of adjacent cells whose values are 1
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -c COLUMN_DELIMITER, --column-delimiter COLUMN_DELIMITER
	                        column delimiter string (default: None)
	  -r ROW_DELIMITER, --row-delimiter ROW_DELIMITER
	                        row delimiter string (default: )
	  -d, --count-diagonals
	                        consider diagonal cells to be adjacent; e.g., [0,0]
	                        and [1,1] would be considered adjacent (default:
	                        False)

##Examples
	$ echo "0101
	0111
	0101" > bitmap.txt
  
Ther are several sample files in the `bitmaps` directory:

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
	[(1, 1), (1, 2), (2, 2), (2, 1)]
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
	[(1, 1), (1, 2), (2, 2), (2, 1)]
	bitmap:
	0101
	0111
	0101
	blocks:
	[(0, 1), (1, 1), (1, 2), (1, 3), (0, 3), (2, 3), (2, 1)]
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
	[(1, 1), (1, 2), (2, 2), (2, 1)]
	[(4, 4)]
	bitmap:
	10001
	01101
	01101
	00001
	00001
	blocks:
	[(0, 0), (1, 1), (1, 2), (2, 2), (2, 1)]
	[(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
	bitmap:
	0101
	0111
	0101
	blocks:
	[(0, 1), (1, 2), (0, 3), (1, 3), (2, 3), (2, 1), (1, 1)]
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
	[(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1)]
	[(2, 3), (3, 3)]
	[(2, 6), (3, 6)]
	[(5, 3), (6, 4), (6, 5), (5, 6)]
