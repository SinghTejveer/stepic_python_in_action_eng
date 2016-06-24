# pylint: disable=invalid-name

"""Heron's formula

Many years ago when Paul went to school, he did not like the Heron's formula
to calculate the area of a triangle, because he considered it very complex.
Once he decided to help all school students: to write and distribute the
program, calculating the area of a triangle by its three sides.

However, there was a problem: as Paul did not like the formula, he did not
memorize it. Help him finish this act of kindness and write the program,
calculating the area of a triangle by the transferred length of its sides,
in accordance with the Heron's formula:

    S = sqrt(p(p − a)(p − b)(p − c))

where p = (a + b + c)/2 – half-perimeter of the triangle. On the input,
the program has integers, and the output should be a real number corresponding
to the area of the triangle.

Sample Input:
    3
    4
    5
Sample Output:
    6.0
"""

import math


def main():
    a = int(input().rstrip())
    b = int(input().rstrip())
    c = int(input().rstrip())

    p = (a + b + c)/2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))

    print(s)

if __name__ == '__main__':
    main()
