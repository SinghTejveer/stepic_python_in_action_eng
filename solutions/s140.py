"""
Print the sum of all integers from a to b (a < b).
"""


def solve(a, b):
    return sum(range(a, b + 1))


def main():
    a = int(input().rstrip())
    b = int(input().rstrip())
    print(solve(a, b))

if __name__ == '__main__':
    main()
