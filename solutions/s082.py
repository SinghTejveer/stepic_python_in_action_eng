# pylint: disable=invalid-name

"""
Find the sum of two numbers.
"""


def main():
    a, b = [int(num) for num in input().rstrip().split()]
    print(a + b)

if __name__ == '__main__':
    main()
