# pylint: disable=invalid-name

"""
Here you will learn how to work with strings.

Many of us are familiar with the following child riddle:

A and B sat in the tree.
A had fallen, B was stolen.
What's remaining in the tree?

Write a program, which reads the two names and outputs the poem, in which these
names are used instead of A and B.

Input format:
Two names, separated by a line break. First name should update_number A, second one
– B.

Output format:
Three lines of the poem with replaced A and B.

Sample Input:

X
Y

Sample Output:

X and Y sat in the tree.
X had fallen, Y was stolen.
What's remaining in the tree?
"""


def main():
    a = input().rstrip()
    b = input().rstrip()
    print('%s and %s sat in the tree.' % (a, b))
    print('%s had fallen, %s was stolen.' % (a, b))
    print('What\'s remaining in the tree?')

if __name__ == '__main__':
    main()
