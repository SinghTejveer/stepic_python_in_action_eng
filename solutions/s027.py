# pylint: disable=invalid-name, too-many-boolean-expressions
# pylint: disable=too-many-branches, too-many-return-statements

"""
Given six real numbers – a, b, c, d, e, f. Solve the following system of linear
equations:

    ax + by = e
    cx + dy = f

    4x + 0y = 5
    0x + 0y = 0

Output format

  - If the system has no solution, then the program should print a single
    number 0.

  - If the system has infinitely many solutions, each of which looks like
    y = kx + b, then the program should print the number 1,
    and then the values k and b.

  - If the system has a single solution (x0, y0), then the program should print
    the number 2, and then the values x0 and y0.

  - If the system has infinitely many solutions that look like x=x0 with any y,
    then the program should output the number 3, and then the value x0.

  - If the system has infinitely many solutions that look like y=y0 with any x,
    then the program should output the number 4, and then the value y0.

  - If any pair of numbers (x,y) is a solution, the program should output
    the number 5.
"""

import sys


def solve(data):
    a, b, c, d, e, f = data

    # Infinite: y = kx + b
    #  - Only one equation
    if not a and not b and not e and c and d and f:
        return [1, -c/d, f/d]
    elif not c and not d and not f and a and b and e:
        return [1, -a/b, e/b]

    #  - Equation can be simplified to each other
    if (all(data) and a/c == b/d == e/f) or \
            (all([a, b, c, d]) and not e and not f and a/c == b/d):
        return [1, -a/b, e/b]

    # Any x and y
    if not any(data):
        return [5]

    # One y and any x
    if not a and not c:
        if not e and not f:
            return [4, 0]
        else:
            try:
                if not b and not e:
                    return [4, f/d]
                elif not d and not f:
                    return [4, e/b]
                elif b/d == e/f:
                    return [4, e/b]
                else:
                    return [0]
            except ZeroDivisionError:
                return [0]

    # One x and any y
    if not b and not d:
        if not e and not f:
            return [3, 0]
        else:
            try:
                if not a and not e:
                    return [3, f/c]
                elif not c and not f:
                    return [3, e/a]
                if a/c == e/f:
                    return [3, e/a]
                else:
                    return [0]
            except ZeroDivisionError:
                return [0]

    # Single solution
    try:
        if d:
            x = (e - b*f/d)/(a - b*c/d)
            y = (f - c*x)/d
            return [2, x, y]
        else:
            x = f/c
            y = (e - a*f/c)/b
            return [2, x, y]
    except ZeroDivisionError:
        return [0]


def nice(num):
    if num % 1 == 0:
        return int(num)
    else:
        return round(num, 6)


def main():
    data = []
    for arg in sys.stdin:
        data.append(float(arg))
    result = solve(data)
    for item in result:
        print(nice(item), end=' ')

if __name__ == '__main__':
    main()
