"""
Fizz Buzz is a classic programming problem. Here is its slightly modified
version.

Write a program that takes the input of two integers: the beginning and the
end of the interval (both numbers belong to the interval).

The program should output the numbers from this interval, but if the number
is divisible by 3, you should output Fizz instead of it, if the number is
divisible by 5 - output Buzz, and if it is divisible both by 3 and by 5 -
output FizzBuzz.

Output each number or the word on a separate line.
"""


def solve(start, stop):
    result = []
    for item in range(start, stop + 1):
        new = ''
        if item % 3 == 0:
            new += 'Fizz'
        if item % 5 == 0:
            new += 'Buzz'
        result.append(new if new else item)
    return result


def main():
    start, stop = [int(x) for x in input().rstrip().split()]
    result = solve(start, stop)
    for item in result:
        print(item)

if __name__ == '__main__':
    main()
