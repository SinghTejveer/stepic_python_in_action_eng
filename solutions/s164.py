"""
In the given string find the longest word and output it.

Input data

Given a string in a single line. Words in the string are separated by a single
space.

Output data

Output the longest word. If there are several such words, you should output the
one, which occurs earlier.
"""


def solve(text: str) -> str:
    return max(text.split(), key=len)


def main():
    text = input().rstrip()
    print(solve(text))

if __name__ == '__main__':
    main()
