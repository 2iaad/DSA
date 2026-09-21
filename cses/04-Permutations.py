# 1070

import sys

# Permutation of N: an array with integers [between 1 and N] + [have no duplicates] + [length of array is exactly N]
# Adjacent: two number sitting next to each other in an array
#   Ex: 4 and 1 are adjacent in => [3, 4, 1, 11]

def main():
    n = int(sys.stdin.readline())

    if (n == 1):
        print(1)
        return

    if n == 2 or n == 3:
        print("NO SOLUTION")
        return

    odd = list(range(1, n + 1, 2))
    even = list(range(2, n + 1, 2))

    even.extend(odd); # add even to the end of odd
    for element in even:
        print(element, end=' ')


if __name__ == "__main__":
    main()