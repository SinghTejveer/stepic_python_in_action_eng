"""The roots of equation

Given the numbers a,b,c,d. Output in ascending order all the integers between
0 and 1000, which are the roots of the equation ax3+bx2+cx+d=0.

If the specified interval does not contain the roots of the equation,
do not output anything.
"""


def solve(a, b, c, d):
    result = []
    for x in range(1001):
        if a*x**3 + b*x**2 + c*x + d == 0:
            result.append(x)
    return result


def main():
    a = int(input().rstrip())
    b = int(input().rstrip())
    c = int(input().rstrip())
    d = int(input().rstrip())

    result = solve(a, b, c, d)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()
