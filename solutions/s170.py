"""
Write a program which finds the percentage of students who have received the A
grade.

Used the five-point grading scale with grades A, B, C, D and F.

Input format:
A single line with student grades separated by a space. There is at least one grade.

Output format:
The floating point number with exactly two digits after the decimal point.

Sample Input 1:

F B A A B C A D

Sample Output 1:

0.38


Sample Input 2:

B C B

Sample Output 2:

0.00


Sample Input 3:

A D

Sample Output 3:

0.50
"""

from typing import List


def solve(grades: List[str]) -> float:
    return round(grades.count('A')/len(grades), 2)


def main():
    grades = input().rstrip().split()
    print('%.02f' % solve(grades))

if __name__ == '__main__':
    main()
