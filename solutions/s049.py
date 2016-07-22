"""
Find the sum of all elements of the sequence, ending with the number 0.

The number 0 itself is not included into the sequence and serves as a sign of
cessation.
"""

import sys


def solve(data):
    return sum(data)


def main():
    data = []
    for num in sys.stdin:
        if num.rstrip() == '0':
            break
        else:
            data.append(int(num.rstrip()))
    print(solve(data))

if __name__ == '__main__':
    main()
