"""
A user inputs a number M. You need to find out what is the smallest integer
n such that n! > M.
"""


def solve(num):
    factorial = 1
    i = 1
    while True:
        factorial *= i
        if factorial > num:
            return i
        i += 1


def main():
    num = int(input().rstrip())
    print(solve(num))

if __name__ == '__main__':
    main()
