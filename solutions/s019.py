"""Swimming pool

Ian was swimming in the pool having size of N×M feets and got tired.
At this moment he realized that he is at a distance of X feets from one of the
long ledge (not necessarily from the nearest one) and Y feets from one of the
short ledges. What is the minimum distance (in feets) Ian needs to swim in order
to reach the swimming pool ledge?

The program input contains numbers N, M, X, Y.

Sample Input:
    23
    52
    8
    43
Sample Output:
    8
"""


def min_distance(height, width, from_longest, from_shortest):
    # Let height be the longest
    height, width = max(height, width), min(height, width)

    return min(from_shortest, from_longest,
               height - from_shortest, width - from_longest)


def main():
    height = int(input().rstrip())
    width = int(input().rstrip())
    from_longest = int(input().rstrip())
    from_shortest = int(input().rstrip())
    print(min_distance(height, width, from_longest, from_shortest))

if __name__ == '__main__':
    main()
