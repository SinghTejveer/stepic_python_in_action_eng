"""
Input of the program is a line containing the words separated by a space.
The program should output the information of lengths of words in the given line,
from the shortest to the longest word (see the example).

A word is a sequence of arbitrary characters surrounded by spaces or line
boundaries. Note that punctuation marks also belong to a word.

Input format:
A string containing a sequence of Latin characters and punctuation marks,
separated by a space.

Output format:
For each word length that appears in the original string, you need to specify
the number of words with such length in a format:

length: amount

Output this information in the order of increasing length.
"""

from collections import Counter

from typing import List


def solve(text: str) -> List[tuple]:
    counter = Counter(len(word) for word in text.split())
    return sorted(counter.most_common())


def main():
    text = input().rstrip()
    result = solve(text)
    for k, v in result:
        print('%d: %d' % (k, v))

if __name__ == '__main__':
    main()
