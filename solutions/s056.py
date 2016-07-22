"""
Write a program, which reads numbers from the input (by one in a line) until
the sum of these numbers will not be equal to 0, and right after this outputs
the sum of the squares of all read numbers.

It is guaranteed that at some moment the sum of the numbers will be equal to 0,
and there is no need to continue reading after this.

In the example, we are reading numbers 1, -3, 5, -6, -10, 13; and at this
moment, we notice that the sum of these numbers is equal to zero, therefore we
output the sum of their squares, not paying attention to the remaining numbers.
"""

import sys


def solve(numbers):
    return sum(num**2 for num in numbers)


def main():
    num_sum = 0
    numbers = []
    for num in sys.stdin:
        num = int(num.rstrip())
        numbers.append(num)
        num_sum += num
        if num_sum == 0:
            break
    print(solve(numbers))

if __name__ == '__main__':
    main()
