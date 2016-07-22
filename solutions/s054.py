"""
Given the sequence of integer numbers (which ends with the number 0).
Find the largest element of the sequence.

The number 0 itself is not included into the sequence, but serves only
as a sign of the end.
"""

import sys


def solve(numbers):
    return max(numbers)


def main():
    numbers = []
    for num in sys.stdin:
        num = int(num.rstrip())
        if num == 0:
            break
        numbers.append(num)
    print(solve(numbers))

if __name__ == '__main__':
    main()
