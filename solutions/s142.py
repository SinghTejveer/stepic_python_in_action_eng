"""
Given the sequence of natural numbers. Find the sum of numbers, divisible by 6.
The input is number of elements in the sequence, and then the elements
themselves. In this sequence, there is always a number, divisible by 6.
"""

import sys


def solve(numbers):
    return sum(num for num in numbers if num % 6 == 0)


def main():
    _ = input()
    numbers = []
    for number in sys.stdin:
        numbers.append(int(number.rstrip()))
    print(solve(numbers))

if __name__ == '__main__':
    main()
