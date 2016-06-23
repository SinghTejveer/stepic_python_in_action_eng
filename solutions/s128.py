"""
Write a program that reads the number and prints YES if it is positive.
Otherwise, the program should print NO.

Sample Input:
    7
Sample Output:
    YES
"""


def main():
    number = int(input().rstrip())
    print('YES' if number > 0 else 'NO')

if __name__ == '__main__':
    main()
