"""
Write a program that checks whether two given words are anagrams.

The program should output True in the case if entered words are anagrams, and
False otherwise.

Input format:

Two words, each on a separate line. Words can only consist of Latin characters.
Your solution should be case insensitive, i.e. characters' case should not
affect the answer.
"""

from collections import Counter


def solve(word1: str, word2: str) -> bool:
    return Counter(word1.lower()) == Counter(word2.lower())


def main():
    word1 = input().rstrip()
    word2 = input().rstrip()
    print(solve(word1, word2))

if __name__ == '__main__':
    main()
