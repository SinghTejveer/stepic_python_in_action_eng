# pylint: disable=invalid-sequence-index

"""Pairwise different summands

Given an integer 1 <= n <= 109 find the maximal number k such that n can be
represented as a sum of pairwise different positive integers. In the first
line output k, in the next line output k summands.
"""

from typing import List


def solve(num: int) -> List[int]:
    i = 1
    summands = []
    while num != 0:
        if num <= 2*i:
            summands.append(num)
            num = 0
        else:
            summands.append(i)
            num -= i
        i += 1
    return summands


def main():
    num = int(input().rstrip())
    result = solve(num)

    print(len(result))
    for item in result:
        print(item, end=' ')


if __name__ == '__main__':
    main()
