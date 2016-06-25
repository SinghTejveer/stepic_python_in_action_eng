"""
Write a program that inputs the distance between the two cities in miles and
the travel time by bus in hours, and outputs the average speed of the bus.

Note: there is NO need to give any explanations during input and output.

Sample Input:

    100
    2

Sample Output:

    50.0
"""


def solve(distance, time):
    return distance/time


def main():
    distance = float(input().rstrip())
    time = float(input().rstrip())
    print('%0.1f' % solve(distance, time))

if __name__ == '__main__':
    main()
