"""
Write a program that reads a three digit number, calculates the new number
by reversing its digits, and outputs a new number.

Sample Input:
    287
Sample Output:
    782
"""


def main():
    num = input().rstrip()
    print(num[::-1])

if __name__ == '__main__':
    main()
