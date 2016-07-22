"""
Write a program, which reads the number of the shape
(1 – square, 2 – circle, 3 – triangle, 4 – rhombus)
and prints the text "You have chosen a square"
(or circle, or triangle, or rhombus, depending on the number).
If it is a number, which doesn't correspond to any of the listed shapes,
the program should output: "There is no such shape!".

Note: output text should exactly match the sample! Including letters case and
location of spaces.

Sample Input:
    1
Sample Output:
    You have chosen a square
"""

SHAPES = {
    '1': 'square',
    '2': 'circle',
    '3': 'triangle',
    '4': 'rhombus',
}


def main():
    choice = input().rstrip()
    try:
        print('You have chosen a %s' % SHAPES[choice])
    except KeyError:
        print('There is no such shape!')

if __name__ == '__main__':
    main()
