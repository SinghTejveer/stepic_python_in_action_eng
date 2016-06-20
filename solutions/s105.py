"""Digital watches

Digital watches display time in the h:mm:ss format (from 0:00:00 to 23:59:59),
i.e. first goes the number of hours, then goes the two-digit number of minutes,
followed by the two-digit number of seconds. If necessary, number of minutes
and seconds are filled by zeroes to a two-digit number.

N seconds passed from the beginning of the day. Output what the watches will
display.

Input data format
    Given the natural number N on input, not exceeding 107107 (10000000).

Sample Input 1:
    3602
Sample Output 1:
    1:00:02

Sample Input 2:
    129700
Sample Output 2:
    12:01:40
"""


def main():
    passed = int(input().rstrip())

    hours = passed//3600
    passed -= hours*3600

    minutes = passed//60
    passed -= minutes*60

    seconds = passed

    print('%d:%02d:%02d' % (hours % 24, minutes, seconds))

if __name__ == '__main__':
    main()
