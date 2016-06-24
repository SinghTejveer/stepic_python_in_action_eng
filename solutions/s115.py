"""Chocolate

A chocolate bar has a shape of rectangle, divided into NxM segments.
You can break down this chocolate bar into two parts by a straight line.
Find whether you can break off exactly K segments from the chocolate.

Input data format
    The program gets an input of three integers: N, M, K

Output data format
    The program must output one of the two words: YES or NO.

Sample Input 1:
    4
    2
    6
Sample Output 1:
    YES

Sample Input 2:
    2
    10
    7
Sample Output 2:
    NO
"""


def main():
    width = int(input().rstrip())
    height = int(input().rstrip())
    parts = int(input().rstrip())

    if any([width*height < parts,
            not width,
            not height,
            width < 0,
            height < 0]):
        print('NO')
    elif parts % width == 0 or parts % height == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
