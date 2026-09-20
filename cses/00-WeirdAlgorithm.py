# 1068

import sys

"""
input: n positive number
if even -> n/2 
if odd  -> n*3 + 1
                -> if even  -> n/2 loop
                -> if odd   -> repeat
"""

def main():

    n = int(sys.stdin.readline());

    print(n, end=' ');

    while (n != 1):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = (n * 3) + 1
        print(n, end=' ');

if __name__ == '__main__':
    main()