# 1072

"""
CSES 1072 - Two Knights (https://cses.fi/problemset/task/1072/)

                                2     2      
                               k  · (k  - 1) 
Max number of Possibilities  = ───────────── 
                                     2
----------------------------------------------------

        W (Columns of Main Board)
    ◄───────────────────────────────►
    ┌───┬───┬───┬───┬───┬───┬───┬───┐ ▲
    │   │   │   │   │   │   │   │   │ │
    ├───┼───┼───┼───┼───┼───┼───┼───┤ │
    │   │ ┌───────────────┐▲│   │   │ │
    ├───┼─│   w columns   ││└───┼───┤ │
    │   │ │ ◄───────────► ││ h rows │ │ H rows
    ├───┼─│               ││┌───┼───┤ │
    │   │ └───────────────┘▼│   │   │ │
    ├───┼───┼───┼───┼───┼───┼───┼───┤ │
    │   │   │   │   │   │   │   │   │ │
    └───┴───┴───┴───┴───┴───┴───┴───┘ ▼

Subgrid Counting Formulas:
┌─────────────────────────────────────────────────────────────┐
│  Vertical Choices   = max(0, H - h + 1)                     │
│                                                             │
│  Horizontal Choices = max(0, W - w + 1)                     │
│                                                             │
│  Total Subgrids     = max(0, H - h + 1) · max(0, W - w + 1) │
└─────────────────────────────────────────────────────────────┘

"""

import sys

# count total subgrids of (2*3 & 3*2) that exist inside the k*k | 2D sliding zindow
def max_knight_placements(k: int, h: int, w: int) -> int:

    vertical_count = k - h + 1
    horizontal_count = k - w + 1

    count = vertical_count * horizontal_count

    return count

def main():

    n = int(sys.stdin.readline())
    print();

    for k in range(1, n + 1):
        
        max_possibilities = (k**2) * (k**2 - 1) // 2 # number of possible ways to place 2 knights in the chessboard

        vertical = max_knight_placements(k, 2, 3)
        horizontal = max_knight_placements(k, 3, 2)

        max_attacks = 2 * (vertical + horizontal) # because 2 of them knights can attack each other.

        print(max_possibilities - max_attacks)

if __name__ == "__main__":
    main()