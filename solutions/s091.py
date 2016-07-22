"""
Find whether the given symbol is a digit.

Output "yes", is the symbol is a digit and "no" otherwise.
Please note that you should output words in a lowercase.
"""


def main():
    print('yes' if input().rstrip().isdigit() else 'no')

if __name__ == '__main__':
    main()
