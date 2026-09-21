# 1069

import sys

"""
input:
    aaavbb
result:
    3

"""

def main():
    string = sys.stdin.readline().strip(); # remove '\n' at the end

    if (len(string) == 0):
        return print(0);

    count, maxLen = 0, 0
    prevChar = string[0]

    for char in string:
        if (prevChar == char):
            count += 1;
        else:
            prevChar = char
            count = 1

        if (count > maxLen):
            maxLen = count

    print(maxLen)

if __name__ == '__main__':
    main()