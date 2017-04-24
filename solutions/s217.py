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
    result = 1
    if exp < 0:
        while exp < 0:
            exp += 1
            result /= num
    else:
        while exp > 0:
            exp -= 1
            result *= num
    return result


def main():
    num = float(input())
    exp = int(input())
    print(solve(num, exp))


if __name__ == '__main__':
    main()
