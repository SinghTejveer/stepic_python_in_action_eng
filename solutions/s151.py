"""
Given the natural number N. Output the word YES, if number N is the exact
power of 2, or NO if otherwise.

Sample Input 1:
    1

Sample Output 1:
    YES


Sample Input 2:
    2

Sample Output 2:
    YES
"""


def solve(num):
    return 'YES' if bin(num).count('1') == 1 else 'NO'


def main():
    num = int(input().rstrip())
    print(solve(num))

if __name__ == '__main__':
    main()
