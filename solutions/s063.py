"""
GC-content is an important feature of the genome sequences and is defined
as the percentage ratio of the sum of all guanines and cytosines to the
overall number of nucleic bases in the genome sequence.

Write a program, which calculates the percentage of G characters (guanine)
and C characters (cytosine) in the entered string. Your program should be
case independent.

For example, in the string "acggtgttat" the percentage of characters G and C
equals to 4/10*100=40.0, where 4 is the number of symbols G and C, and 10
is the length of the string.
"""


def solve(genome):
    genome = genome.lower()
    return (genome.count('g') + genome.count('c'))/len(genome)*100


def main():
    genome = input().rstrip()
    print(solve(genome))

if __name__ == '__main__':
    main()
