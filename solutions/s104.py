"""Difference of times

Given the values of the two moments in time in the same day: hours, minutes
and seconds for each of the time moments. It is known that the second moment
in time happened not earlier than the first one. Find how many seconds passed
between these two moments of time.

Input data format
    The program gets the input of the three integers: hours, minutes, seconds,
    defining the first moment of time and three integers that define the second
    moment time.

Output data format
    Output the number of seconds between these two moments of time.

Sample Input 1:
    1
    1
    1
    2
    2
    2
Sample Output 1:
    3661

Sample Input 2:
    1
    2
    30
    1
    3
    20
Sample Output 2:
    50
"""

import sys


def main():
    h1 = int(input().rstrip())
    m1 = int(input().rstrip())
    s1 = int(input().rstrip())

    h2 = int(input().rstrip())
    m2 = int(input().rstrip())
    s2 = int(input().rstrip())

    print(h2*60*60 + m2*60 + s2 - h1*60*60 - m1*60 - s1)

if __name__ == '__main__':
    main()
