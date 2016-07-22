"""Standard Deviation

Given a sequence of natural numbers x1, x2, ..., xn.

Input data format

Given a sequence of integers, ending with number 0. Find the standard deviation
of this sequence.

There are at least two numbers in the sequence.The number 0 itself is not
included into the sequence and serves as a sign of cessation.
"""

import math
import sys


def solve(numbers):
    average = sum(numbers)/len(numbers)
    return math.sqrt(sum((x - average)**2 for x in numbers)/(len(numbers) - 1))


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
