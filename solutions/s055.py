"""
Write a program that prints a part of the sequence
    1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...

(the number is repeated as many times, to what it equals to).
Input to the program is a positive integer n – the number of the elements of
the sequence the program should print. On the output, it is expected to get the
sequence of numbers, written in a single line, space-separated.

For example, if n = 7, then the program should output 1 2 2 3 3 3 4.
"""


def solve(limit):
    result = []
    i = 0
    while True:
        i += 1
        for _ in range(i):
            result.append(i)
            limit -= 1
            if not limit:
                return result


def main():
    limit = int(input().rstrip())
    result = solve(limit)
    for item in result:
        print(item, end=' ')

if __name__ == '__main__':
    main()
