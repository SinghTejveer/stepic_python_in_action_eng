"""The number of tens

Given a non-negative integer N (0 ≤ N ≤ 1000000), find the number of tens in it
(i.e. next to last digit of the number). If there is no next to last digit, you
can consider that the number of tens equals to zero.

Sample Input:
    73
Sample Output:
    7
"""


def main():
    num = input().rstrip()
    try:
        print(num[-2])
    except IndexError:
        print(0)

if __name__ == '__main__':
    main()
