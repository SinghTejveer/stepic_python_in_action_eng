"""
Given a string. Find whether it is a palindrome, i.e. it reads the same both
left-to-right and right-to-left. Output “yes” if the string is a palindrome
and “no” otherwise.
"""


def solve(text: str) -> bool:
    return text == text[::-1]


def main():
    text = input().rstrip()
    print('yes' if solve(text) else 'no')

if __name__ == '__main__':
    main()
