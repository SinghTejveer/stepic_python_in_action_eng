"""
Write a program that reads an integer from the input (a non-negative one),
and outputs this number to the console together with a correctly changed word
"contig", for example: 1 contig, 5 contigs.
"""


def solve(num: int) -> str:
    return '%d contig' % num + ('s' if num != 1 else '')


def main():
    num = int(input().rstrip())
    print(solve(num))

if __name__ == '__main__':
    main()
