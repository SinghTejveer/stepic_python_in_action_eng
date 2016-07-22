"""Symmetrical number

Given a four-digit number. Determine whether its decimal notation is symmetric.
If the number is symmetrical, output 1, otherwise output any other integer.
The number may have less than four digits, then you should assume that its
decimal notation is complemented by insignificant zeros on the left.

Sample Input 1:
    2002
Sample Output 1:
    1

Sample Input 2:
    2008
Sample Output 2:
    37
"""


def symmetrical(num):
    str_num = str(num).zfill(4)
    return str_num[:2] == str_num[-1] + str_num[-2]


def main():
    number = int(input().rstrip())
    print(1 if symmetrical(number) else 0)

if __name__ == '__main__':
    main()
