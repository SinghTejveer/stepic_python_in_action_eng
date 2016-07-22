"""Fractional part 1

Given a positive real number X. Output its fractional part.

Sample Input:
    17.9
Sample Output:
    0.9
"""


def main():
    num = input().rstrip()
    try:
        print('0.' + num.split('.')[1])
    except IndexError:
        print('0')

if __name__ == '__main__':
    main()
