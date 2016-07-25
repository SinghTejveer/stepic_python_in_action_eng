"""
Given a sequence of integers. Find any of its longest increasing subsequences.

The sequence is given in the form of numbers separated by spaces on a single
line.

Output the subsequence in a single line, space separated.

Sample Input 1:
1 2 3 4 5
Sample Output 1:
1 2 3 4 5

Sample Input 2:
1 4 4 3 5 2 8
Sample Output 2:
1 4 5 8

Sample Input 3:
1 3 5 2 4
Sample Output 3:
1 3 5
"""


def solve(sequence):
    longest = []
    sequences = []

    for i, item in enumerate(sequence):
        # Update founded sequences
        for seq in sequences[:]:
            # There're not enough elements
            if len(sequence) - i - 1 < len(longest) - len(seq):
                sequences.remove(seq)
                continue

            if item > seq[-1]:
                sequences.append(seq[:])
                seq.append(item)

            if len(seq) > len(longest):
                longest = seq

        # There're not enough elements
        if len(sequence) - i > len(longest):
            sequences.append([item])
            if not longest:
                longest = [item]

    return longest


def main():
    sequence = list(map(int, input().rstrip().split()))
    result = solve(sequence)
    for item in result:
        print(item, end=' ')

if __name__ == '__main__':
    main()
