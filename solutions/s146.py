"""
The interest rate on the deposit is P percent per annum, which are added to the
deposit amount after one year. The deposit is X dollars Y cents. Find the size
of the deposit in K years.

Input data format

Integers P, X, Y, K.

Output data format

The program should output two numbers: the size of the deposit in K years in
dollars and cents. Fractional parts of cents after a year should be discarded.
Recalculation of the deposit amount (discarding the fractional parts of cents)
occurs annually.

Note: If you are facing issues with accuracy in this problem – try to solve it
using only integer numbers.

Sample Input:

    12
    179
    0
    5

Sample Output:

    315 43
"""

import decimal


def solve(percent, dollars, cents, years):
    deposit = decimal.Decimal(str(dollars) + '.' + str(cents))
    for _ in range(years):
        new = decimal.Decimal(deposit*percent/100)
        deposit += new
        deposit = deposit.quantize(
            decimal.Decimal('.01'), rounding=decimal.ROUND_FLOOR)
    result_dollars = int(deposit)
    result_cents = int((deposit % 1)*100)

    return [result_dollars, result_cents]


def main():
    percent = int(input().rstrip())
    dollars = int(input().rstrip())
    cents = int(input().rstrip())
    years = int(input().rstrip())

    new_dollars, new_cents = solve(percent, dollars, cents, years)
    print(new_dollars, end=' ')
    print(new_cents)

if __name__ == '__main__':
    main()
