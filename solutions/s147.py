"""
A detector compares the size of parts produced by a machine with the reference
standard.

If the size of the part is larger, it can be sent to be fixed, and the detector
prints the number 1. If the size of the part is smaller, it is removed as
reject, and the detector prints the number -1. If the part was made perfect,
it is sent to the box with ready products, and the detector prints 0.

Write a program, which takes the number of parts n as input, and then the
sequence of detector prints. The program should output numbers in a single
line – the number of ready parts, the number of parts to be fixed, and the
number of rejects.
"""

import sys


def solve(data):
    ready, fixed, rejected = 0, 0, 0
    for item in data:
        if item == 0:
            ready += 1
        elif item == 1:
            fixed += 1
        elif item == -1:
            rejected += 1
    return [ready, fixed, rejected]


def main():
    _ = input()
    data = []
    for item in sys.stdin:
        data.append(int(item.rstrip()))
    result = solve(data)
    for item in result:
        print(item, end=' ')

if __name__ == '__main__':
    main()
