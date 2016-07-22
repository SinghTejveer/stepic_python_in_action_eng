"""
You decided to write a converter from Python code into Java code. As CamelCase
names are standard in Java, you decided to learn how to convert names from
underscore into this format.

First, write a program, which changes variable names from underscore to the
UpperCamelCase style.

In the underscore style each word starts from a lowercase letter characterizes,
and the underscore character “_” separates the words. In the UpperCamelCase
style each word is starts from the capital letter and there are no separators
between the words.

Input format:
Single string, containing the name, written in the underscore style.

Output format:
The string, containing the new name in the UpperCamelCase style.
"""


def solve(variable: str) -> str:
    return ''.join(x.capitalize() for x in variable.split('_'))


def main():
    variable = input().rstrip()
    print(solve(variable))

if __name__ == '__main__':
    main()
