"""
Find the number of "Ds", "Cs", "Bs" and "As" for the last test on informatics
in the class consisting of n students. The program gets number n as input,
and then gets the grades themselves (one by one). The program should output
four numbers in a single line - the number of "D", the number of "C",
the number of "B" and the number of "A" grades.
"""

import sys


def solve(grades):
    return [grades.count(2), grades.count(3), grades.count(4), grades.count(5)]


def main():
    grades = []
    _ = int(input().rstrip())
    for grade in sys.stdin:
        grades.append(int(grade.rstrip()))
    result = solve(grades)
    for item in result:
        print(item, end=' ')

if __name__ == '__main__':
    main()
