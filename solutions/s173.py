"""
Write a program that finds all occurrences of the given substring in the string.

Input format:
The first line of input contains the original string, the second line contains
the substring, the positions of which you should find. The lines consist of
Latin characters only.

Output format:
A single line with the indices (indexing starts with zero) of the occurrences
of the given substring in the string, separated by a space, or number -1
when the substring is absent.
"""

import re

from typing import List


def solve(text: str, substring: str) -> List:
    result = [m.start() for m in re.finditer(r'(?=%s)' % substring, text)]
    return result if result else [-1]


def main():
    text = input().rstrip()
    substring = input().rstrip()
    for position in solve(text, substring):
        print(position, end=' ')

if __name__ == '__main__':
    main()
