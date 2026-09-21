# 1083

import sys

"""
input:
-> n
-> (n - 1) numbers

5
4 3 1 2

"""

def main():
    count = 0
    n = int(sys.stdin.readline()) # store element as integer

    numbers = sys.stdin.readline().split() # split using whitespaces => ["4", "3", "1", "2"]
    numbers = map(int, numbers) # apply int(x) to each element of the array => [4, 3, 1, 2]
    numbers = list(numbers) # put numbers in a vector

    count = sum(range(1, n + 1)) # or use this formula n * (n + 1) / 2
    numbers = sum(numbers)

    print(count - numbers);

if __name__ == "__main__":
    main()