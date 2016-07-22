"""
Given the natural number 1 <= n <= 10^5 and the array of integers A[1…n],
not exceeding 10^9 by absolute value. Output 1, if the array A contains the
number occurring strictly more than n/2 times, and output 0 otherwise.

Sample Input:
5
2 3 9 2 2
Sample Output:
1
"""

from typing import List


def solve(array: List[int]) -> int:
    array = sorted(array)
    count = 0
    for i, item in enumerate(array):
        if count > len(array)/2:
            return 1
        elif len(array) - i <= len(array)/2 - count:  # Not enough elements
            return 0
        elif i == 0 or item == array[i-1]:
            count += 1
        else:
            count = 1


def main():
    _ = input()
    array = [int(item) for item in input().rstrip().split()]
    print(solve(array))

if __name__ == '__main__':
    main()
