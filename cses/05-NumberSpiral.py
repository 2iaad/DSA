# 1071

"""
CSES 1071 - Number Spiral (https://cses.fi/problemset/task/1071)

- List vs Tuple:
    * list: `[]` (like C++ vector). can be modified, dynamic, cannot be hashed in set/dict.
    * tuple: `(x, y)` (like const std::pair). read-only, fixed size, hashable.
    * Commas create tuples: `(5,)` is a tuple; `(5)` is just an int (grouping parens).
    * `[]` is faster than `list()`; use `list()` only for type conversion.

- Conventions & Syntax:
    * Functions and variables use `snake_case` (PEP 8).
    * `for _ in range(t):` indicates an unused loop counter.
"""

import sys

def extract_value(point):
    y, x = point;

    squar = max(x, y) # identifying which layer we are in
    if squar == x:
        if (squar % 2 != 0): # odd
            biggest_element = squar ** 2
            result = biggest_element - (y - 1)
        else:
            smallest_element = (squar - 1) ** 2 + 1
            result = smallest_element + (y - 1)

    if squar == y:
        if (squar % 2 != 0): #odd
            smallest_element = (squar - 1) ** 2 + 1
            result = smallest_element + (x - 1)
        else:
            biggest_element = squar ** 2
            result = biggest_element - (x - 1)

    print(result)


def main():
    t = int(sys.stdin.readline())
    
    points = [] # create list (or vector in c++) ----- we can also do list()
    # print(type(points))

    for _ in range(t):

        point = tuple(map(int, sys.stdin.readline().split())) # create tuple (or std::pair<int, int> in c++)

        points.append(point);

    for element in points:
        extract_value(element)

if __name__ == "__main__":
    main()