"""The smallest natural divisor

Given an integer, not less than 2. Find its smallest natural divisor,
different from 1.
"""


def solve(num):
    i = 2
    while True:
        if num % i == 0:
            return i
        i += 1


def main():
    num = int(input().rstrip())
    print(solve(num))

if __name__ == '__main__':
    main()
