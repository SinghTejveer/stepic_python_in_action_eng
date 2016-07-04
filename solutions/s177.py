"""
Write a program that reads integers from the input one number per line.

For each of the entered numbers please check:
if the number is less than 10, then skip that number;
if the number is greater than 100, then stop reading numbers;
in any other cases bring the number back to the console in a separate line.
"""

import sys


def main():
    for line in sys.stdin:
        number = int(line.rstrip())
        if number > 100:
            break
        if number > 9:
            print(number)

if __name__ == '__main__':
    main()
