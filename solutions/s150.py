"""
Given integer N. Print all the squares of natural numbers, not exceeding N,
in ascending order.
"""

import math


def solve(limit):
    return [x*x for x in range(1, int(math.sqrt(limit)) + 1)]


def main():
    limit = int(input().rstrip())
    result = solve(limit)
    for item in result:
        print(item)

if __name__ == '__main__':
    main()
