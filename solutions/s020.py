"""Triangle

Given three natural numbers A, B, C. Define if the triangle with such sides
exists.

If the triangle exists - output the YES string, otherwise - output NO.

Triangle is a three points that are not located on a single straight line.

Sample Input:
    3
    4
    5
Sample Output:
    YES
"""


def is_triangle(side1, side2, side3):
    sides = [side1, side2, side3]

    longest = max(side1, side2, side3)
    shortest = min(side1, side2, side3)
    middle = sum(sides) - longest - shortest

    return 'YES' if middle > longest - shortest else 'NO'


def main():
    side1 = int(input().rstrip())
    side2 = int(input().rstrip())
    side3 = int(input().rstrip())

    print(is_triangle(side1, side2, side3))

if __name__ == '__main__':
    main()
