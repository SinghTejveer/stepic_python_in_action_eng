"""Huffman coding

Given non-empty string sof length not more than 104, consisting of lowercase
letters of the Latin alphabet. Construct an optimized prefix-free code. In the
first line output the number of various letters k, which are present in the
string, and the size of the resulting encoded string. In the next k lines write
letter codes in the "letter: code" format. In the last line output
the encoded string.
"""

from collections import Counter
from heapq import heappush, heappop, heapify


def encode(frequency):
    if len(frequency) == 1:
        return [[key, '0'] for key in frequency.keys()]

    heap = [[weight, [letter, '']] for letter, weight in frequency.items()]
    heapify(heap)

    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return heappop(heap)[1:]


def main():
    text = input().rstrip()
    letter_codes = encode(Counter(text))
    codes_dict = {k: v for k, v in letter_codes}
    encoded_text = ''.join(codes_dict[letter] for letter in text)

    print(len(codes_dict), len(encoded_text))
    for letter, code in letter_codes:
        print('%s: %s' % (letter, code))
    print(encoded_text)

if __name__ == '__main__':
    main()
