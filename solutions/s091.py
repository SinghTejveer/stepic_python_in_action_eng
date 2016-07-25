"""Cover intervals with points

Given n intervals. Find the set of points having the minimum size (cardinality),
for which each of the given intervals contains at least one of the points.

The first line given 1≤n≤100 - number of intervals. Each of the next n lines
contains two 0<=l<=r<=109 numbers, setting the beginning and the end of
the interval. Output the minimum size of the set m and the m points themselves.
If there are several such sets, output any of them.
"""

import sys
from operator import itemgetter


def solve(intervals):
    dots = []
    left = -1

    for interval in sorted(intervals, key=itemgetter(1)):
        if interval[0] > left:
            dots.append(interval[1])
            left = interval[1]
    return dots


def main():
    intervals = []
    _ = input()
    for line in sys.stdin:
        start, end = line.rstrip().split()
        intervals.append((int(start), int(end)))

    dots = solve(intervals)

    print(len(dots))
    for dot in dots:
        print(dot, end=' ')


if __name__ == '__main__':
    main()
