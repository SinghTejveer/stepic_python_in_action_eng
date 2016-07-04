# pylint: disable=invalid-name, invalid-sequence-index

"""
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d
(with space in between), inclusively.
"""

import os

from typing import List


def solve(text: str, indexes: List[int]) -> List[str]:
    a, b, c, d = indexes
    return [text[a:b+1], text[c:d+1]]


def main():
    with open(os.path.join('datasets', 's176.txt')) as data_file:
        text, indexes = data_file.readlines()
    indexes = [int(index) for index in indexes.split()]
    first, second = solve(text, indexes)
    print('%s %s' % (first, second))

if __name__ == '__main__':
    main()
