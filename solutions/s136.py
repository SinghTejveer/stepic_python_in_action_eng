# pylint: disable=invalid-name

"""Arithmetic average

Write a program that reads two numbers a and b from the keyboard, calculates
and outputs to the console the arithmetic average of all numbers from the
interval [a;b], which are divided by 3.

In the example below the arithmetic average is calculated for the numbers on
the interval [−5;12]. Total numbers divided by 3 on this interval 6:
−3, 0, 3, 6, 9, 12. Their arithmetic average equals to 4.5

The program input contains intervals, which always contain at least one number,
which is divided by 3.

Sample Input:
    -5
    12

Sample Output:
    4.5
"""


def solve(a, b):
    nums = [x for x in range(a, b + 1) if x % 3 == 0]
    return sum(nums)/len(nums)


def main():
    a = int(input().rstrip())
    b = int(input().rstrip())
    print(solve(a, b))

if __name__ == '__main__':
    main()
