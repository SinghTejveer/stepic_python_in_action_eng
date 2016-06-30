"""The average value

Given the sequence of integers, ending with number 0. Find the average value
of all elements in this sequence.

The number 0 itself is not included into the sequence and serves just as a
sign of cessation.
"""

import sys


def solve(numbers):
    return sum(numbers)/len(numbers)


def main():
    numbers = []
    for num in sys.stdin:
        num = int(num.rstrip())
        if not num:
            break
        else:
            numbers.append(num)
    print(solve(numbers))

if __name__ == '__main__':
    main()
