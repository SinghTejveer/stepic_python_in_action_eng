"""
You are given an integer number of indefinite length. Check, whether this
number divides by 3 or not, without using the remainder (%) operation.

Print "YES" if the number divides by 3 and "NO" if it doesn't.

Note: What happens, when you divide, say, 17 by 3? And then back.
"""


def solve(num):
    return 'YES' if (num//3)*3 == num else 'NO'


def main():
    num = int(input().rstrip())
    print(solve(num))

if __name__ == '__main__':
    main()
