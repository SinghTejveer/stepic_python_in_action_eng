"""Purchase pies

A pie costs A dollars and B cents. Find how many dollars and cents you need
to pay for N pies.

Input data format
    The program gets three numbers as input: A, B, N - integers, positive,
    don't exceed 10000.

Output data format
    The program should output two numbers separated by a space: cost of the
    purchase in dollars and cents.

Sample Input 1:
    10
    15
    2
Sample Output 1:
    20 30

Sample Input 2:
    2
    50
    4
Sample Output 2:
    10 0
"""


def count_coins(dollars, cents, pies):
    dollar_num = pies*dollars
    cent_num = pies*cents

    dollars_instead_cents = cent_num//100
    cent_num -= dollars_instead_cents*100
    dollar_num += dollars_instead_cents

    return dollar_num, cent_num


def main():
    dollars = int(input().rstrip())
    cents = int(input().rstrip())
    pies = int(input().rstrip())

    print(*count_coins(dollars, cents, pies))

if __name__ == '__main__':
    main()
