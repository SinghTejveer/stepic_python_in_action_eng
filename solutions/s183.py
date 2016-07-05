"""
Write a program, which turns a sequence of integers x1,x2,…,xn into the
sequence (x1+xn),(x2+xn−1),(x3+xn−2),… of length ⌈n/2⌉.

Input format: input is a positive integer n<106, next go the n integers
separated by spaces, corresponding to x1,…,xn.

Output format: the output should be the ⌈n/2⌉
space-separated integers, corresponding to the sequence (x1+xn),(x2+xn−1),
(x3+xn−2),…. In the case if number n is an odd one, x(n+1)/2 (i.e. the average
number of the array) should serve as the last element of the sequence.

Sample Input:

10 30 32 43 65 -32 54 34 -23 11 9

Sample Output:

39 43 20 99 22
"""


def solve(numbers):
    result = []
    for i in range(len(numbers)//2):
        result.append(numbers[i] + numbers[-i-1])
    if len(numbers) % 2 != 0:
        result.append(numbers[len(numbers)//2])
    return result


def main():
    _, *numbers = [int(num) for num in input().rstrip().split()]
    for item in solve(numbers):
        print(item, end=' ')

if __name__ == '__main__':
    main()
