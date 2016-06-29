"""
Given a sequence of natural numbers, not exceeding 30000. Find the its maximum
element divisible by 4. As input, the program gets the number of elements
in the sequence, and then the elements themselves. In the sequence,
there is always an element divisible by 4. The number of elements does
not exceed 1000. The program should print the single number – the maximum
element of the sequence divisible by 4.
"""

import sys


def solve(numbers):
    return max(num for num in numbers if num % 4 == 0)


def main():
    _ = input()
    numbers = []
    for number in sys.stdin:
        numbers.append(int(number.rstrip()))
    print(solve(numbers))

if __name__ == '__main__':
    main()
