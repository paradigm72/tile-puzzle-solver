Tile Puzzle Solver

Simple program to calculate the correct orientation for a 3x3 "Scramble Square" tile puzzle. Each of the 4 edges of each piece will have one of 4 styles, and that style will match one of the other styles which is an edge on the adjacent piece.

At initialization, each square is encoded with a 4-character representation, in TRBL order. a, b, c, and d are the bottoms of the pattern, and 1, 2, 3, and 4 are the tops. Square and Path are represented as custom Python classes, though mostly just as a way to organize state and methods.

The algorithm is recursive brute force: each starting square is attempted, and then for each possible next square, each of the 4 possible rotations is attempted. During the path construction, a grid representation is maintained. At the end, we checking linear adjacent edges, since those are difficult to check when evaluating a new potential square in the path. That final filtering reduces the set of valid paths to only those that are translated from or in the rotation symmetry group of the correct answer; this result seems to show there is only one configuration that works.
