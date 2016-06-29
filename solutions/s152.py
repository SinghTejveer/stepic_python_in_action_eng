"""
On the input, the program gets a sequence of non-negative integers; each
integer is written in a separate line. The sequence ends with an integer 0,
when reading which the program should end its work and output the length of
the sequence (not counting the final 0).

Don’t read numbers following the number 0.
"""

import sys


def solve(data):
    length = 0
    for item in data:
        if item == 0:
            break
        else:
            length += 1
    return length


def main():
    data = []
    for num in sys.stdin:
        data.append(int(num.rstrip()))
    print(solve(data))

if __name__ == '__main__':
    main()
