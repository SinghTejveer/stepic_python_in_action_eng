"""Fractional part 2

Given a positive real number X. Output its first digit after the decimal point.

Sample Input:
    1.79
Sample Output:
    7
"""


def main():
    num = input().rstrip()
    try:
        print(num.split('.')[1][0])
    except IndexError:
        print(0)

if __name__ == '__main__':
    main()
