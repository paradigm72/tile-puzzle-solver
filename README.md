Tile Puzzle Solver

Simple program to calculate the correct orientation for a 3x3 square tile puzzle. Each of the 4 edges of each piece will have one of 4 styles, and that style will match one of the other styles which is an edge on the adjacent piece.

At initialization, each square is encoded with a 4-character representation, in TRBL order. a, b, c, and d are the bottoms of the pattern, and 1, 2, 3, and 4 are the tops.

The algorithm is recursive brute force: each starting square is attempted, and then for each possible next square, each of the 4 possible rotations is attempted. As it currently stands (Dec 2020), this produces around 7,000 correct length-9 paths, because we aren't yet checking for sideways edge matches.
