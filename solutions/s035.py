# pylint: disable=invalid-name

"""
Given real numbers a, b, c, where a ≠ 0.

Solve the quadratic equation ax2 + bx + c = 0 and output all of its roots.

If the equation has two roots, output these two roots in ascending order; if
one root - output a single number; if no roots – do not output anything.

Sample Input:
    1
    -1
    -2

Sample Output:
    -1 2
"""

import math


def solve(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return ()
    elif d == 0:
        x = -b/(2*a)
        return (x,)
    else:
        x1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        return tuple(sorted((x1, x2)))


def main():
    a = float(input().rstrip())
    b = float(input().rstrip())
    c = float(input().rstrip())

    result = solve(a, b, c)
    print(' '.join(str(x) for x in result))

if __name__ == '__main__':
    main()
