"""
Write a program, which reads two integers a and b (separated by a line break),
and outputs the value of a**b. The operator ** is used in Python for
exponentiation.

Sample Input:
    16
    64
Sample Output:
    115792089237316195423570985008687907853269984665640564039457584007913129639936
"""


def main():
    num = int(input().rstrip())
    power = int(input().rstrip())
    print(num**power)

if __name__ == '__main__':
    main()
