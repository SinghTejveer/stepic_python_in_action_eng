"""
Upon learning that DNA is not a random string, freshmen of the Bioinformatics
Institute from the informatics group suggested using a compression algorithm
that compresses repeated characters in a string.

Encoding is performed as follows:
s = 'aaaabbсaa' is converted into 'a4b2с1a2', that is, the groups of the same
characters of the input string are replaced by the symbol and the number of its
repetitions in this string.

Write a program, which reads the string, encodes it by this algorithm and
outputs the encoded sequence. Encoding must be case sensitive.
"""


def solve(dna):
    if not dna:
        return ''

    result = ''
    count = 0
    for i, current in enumerate(dna):
        if i == 0 or current == dna[i-1]:
            count += 1
        else:
            result += dna[i-1] + str(count)
            count = 1
    return result + dna[-1] + str(count)


def main():
    dna = input().rstrip()
    print(solve(dna))

if __name__ == '__main__':
    main()
