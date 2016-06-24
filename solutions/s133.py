"""Deposit-1

The interest rate on the deposit is P percent per annum, which are added to the
deposit amount at the end of the year. The deposit is X rubles and Y kopecks.
Find the deposit amount a year after.

You are not allowed to use conditional statements and loops when solving this
problem.

Input data format
    Given integers P, X, Y.

Output data format
    The program should output two numbers: the size of the deposit in rubles and
    kopecks after one year. The fractional part of kopecks should be discarded.

Sample Input:
    12
    179
    0

Sample Output:
    200
    48
"""

import decimal


def interest(percent, rubles, kopecks):
    deposit = decimal.Decimal(str(rubles) + '.' + str(kopecks))
    new = deposit*percent/100
    new_rounded = new.quantize(
        decimal.Decimal('.01'), rounding=decimal.ROUND_05UP)
    result = deposit + new_rounded

    result_rubles = int(result)
    result_kopecks = int((result % 1)*100)

    return result_rubles, result_kopecks


def main():
    percent = int(input().rstrip())
    rubles = int(input().rstrip())
    kopecks = int(input().rstrip())

    result_rubles, result_kopecks = interest(percent, rubles, kopecks)
    print(result_rubles)
    print(result_kopecks)

if __name__ == '__main__':
    main()
