"""
Given number N. Print all integer powers of two, not exceeding N,
in ascending order.

Sample Input:

50

Sample Output:

1
2
4
8
16
32
"""


def solve(limit):
    result = []
    i = 0
    while True:
        item = 2**i
        if item > limit:
            break
        result.append(item)
        i += 1
    return result


def main():
    limit = int(input().rstrip())
    result = solve(limit)
    for num in result:
        print(num)

if __name__ == '__main__':
    main()
