# 1094

import sys

"""
Input:
    5
    3 2 5 1 7

Output:
    5
"""

def main():
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    moves = 0

    for index in range(1, n):
        if (array[index] < array[index - 1]):
            moves += array[index - 1] - array[index]
            array[index] = array[index - 1]

    print(moves)

if __name__ == "__main__":
    main()