"""
You are given coordinates of two queens on a chess board.
Find out, whether they hit each other or not.

INPUT
    Four integer numbers x1,y1,x2,y2 are being typed.

OUTPUT
    Type "YES" (uppercase) if they hit each other or "NO" if the don't.

You may need the function, that calculates the absolute magnitude of the number,
here it is: a = abs(a) # writes |a| into 'a' variable

Sample Input 1:
    1 1 3 3
Sample Output 1:
    YES

Sample Input 2:
    1 1 4 3
Sample Output 2:
    NO

Sample Input 3:
    2 2 5 2
Sample Output 3:
    YES
"""

from collections import namedtuple

Queen = namedtuple('Queen', 'x y')


def main():
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    queen1 = Queen(x1, y1)
    queen2 = Queen(x2, y2)

    # Same column
    if queen1.x == queen2.x:
        print('YES')

    # Same row
    elif queen1.y == queen2.y:
        print('YES')

    # First diagonal
    elif queen1.x - queen1.y == 0 == queen2.x - queen2.y:
        print('YES')

    # Second diagonal
    elif abs(queen1.x - queen2.x) == abs(queen1.y - queen2.y):
        print('YES')

    else:
        print('NO')


if __name__ == '__main__':
    main()
