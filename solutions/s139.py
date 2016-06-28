"""
In the Bioinformatics Institute a competition is held between the computer
science and biology students. The winners will get a large and tasty pie.
The team of biology students consists of a students, computer science team — b
students.

It is necessary to pre-cut the pie so that it would be possible to distribute
the pieces of the pie to any team that won the competition, with each member
of this team should get the same number of pieces of the pie. And since you
do not want to cut the pie into the too many small pieces, you need to find
the minimum suitable number.

Write a program, which helps to find this number.

The program gets the size of the teams (two positive integers a
and b, each number is entered in a separate line) and should output the
smallest number d, which is divisible by both numbers without remainder.
"""

from fractions import gcd


def solve(a, b):
    return int(a*b/gcd(a, b))


def main():
    a = int(input().rstrip())
    b = int(input().rstrip())
    print(solve(a, b))

if __name__ == '__main__':
    main()
