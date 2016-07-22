"""Squirrels and nuts - 1

N squirrels found K nuts and decided to divide them equally. Determine how many
nuts each squirrel will get.

Input data format
    There are two positive numbers N and K, each of them is not greater than
    10000.

Sample Input:
    3
    14

Sample Output:
    4
"""


def main():
    squirrels = int(input().rstrip())
    nuts = int(input().rstrip())
    print(nuts//squirrels)

if __name__ == '__main__':
    main()
