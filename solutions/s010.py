"""The sum of digits of a three-digit number

Given a three-digit integer (i.e. an integer from 100 to 999).
Find the sum of its digits.

Sample Input:
    476
Sample Output:
    17
"""


def main():
    num = int(input().rstrip())
    num_sum = sum(int(char) for char in str(num))
    print(num_sum)

if __name__ == '__main__':
    main()
