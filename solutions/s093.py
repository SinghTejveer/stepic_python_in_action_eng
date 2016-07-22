# pylint: disable=invalid-sequence-index

"""Continuous backpack

First line contain the number of items 1 <= n <= 10^3 and capacity of the
backpack 0 <= W <= 2*10^6. Each of the next n lines specifies the cost
0 <= ci <= 2*10^6 and volume 0 < wi <= 2*10^6 of an item (n, W, ci, wi
— integers). Output the maximum cost of parts of the items (you can separate
any part from each item, its cost and volume will decrease proportionally),
placed in the backpack, with an accuracy of not less than three decimal places.
"""

import sys

from typing import List


def solve(capacity: int, items: List[int]) -> float:
    sum_cost = 0

    for cost, volume in sorted(items, key=lambda x: x[0]/x[1], reverse=True):
        if volume < capacity:
            capacity -= volume
            sum_cost += cost
        else:
            return sum_cost + capacity*cost/volume
    return sum_cost


def main():
    _, capacity = input().rstrip().split()
    items = []

    for line in sys.stdin:
        cost, volume = line.rstrip().split()
        items.append((int(cost), int(volume)))

    result = solve(int(capacity), items)
    print('%.3f' % result)

if __name__ == '__main__':
    main()
