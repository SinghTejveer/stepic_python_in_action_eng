"""
At some point, you got tired of using the file names with spaces and you have
decided to write a program that renames all files that contain spaces in their
names by replacing the groups of spaces by the underscore symbol "_".

First, you need to write a program that reads the string and replaces the group
of white space characters by underscore symbols.

Input format:
Single line, containing arbitrary symbols, including spaces.

Output format:
Modified string.
"""


def solve(filename: str) -> str:
    return '_'.join(filename.split())


def main():
    filename = input().rstrip()
    print(solve(filename))

if __name__ == '__main__':
    main()
