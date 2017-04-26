"""Given a real positive number a and an integer number n.

Find a**n.  You need to write the whole program with a recursive function
power(a, n).

Sample Input 1:
    2
    1
Sample Output 1:
    2

Sample Input 2:
    2
    2
Sample Output 2:
    4
"""


def solve(num: float, exp: int) -> float:
    """Calculate num**exp."""
    if exp < 0:
        return solve(1 / num, -exp)
    elif exp == 0:
        return 1
    elif exp == 1:
        return num
    elif exp % 2 == 0:
        return solve(num * num, exp // 2)
    else:
        return num * solve(num * num, (exp - 1) // 2)


def main():
    num = float(input())
    exp = int(input())
    print(solve(num, exp))


if __name__ == '__main__':
    main()
