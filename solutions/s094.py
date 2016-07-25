"""Huffman decoding

Restore the string by its code and the prefix-free code of symbols.

The first line of the input file specifies the two integers k and l separated
by a space — the amount of various characters in the string and the size of the
resulting encoded string, accordingly. The next k lines contain letter codes in
the "letter: code" format. None of the codes is a prefix of another one.
Letters can be listed in any order. Letters can be only the lowercase letters
of the Latin alphabet; each of these letters occurs in the string at least once.
Finally, the last line contains an encoded string. The original string and the
codes of all the letters are not empty. The specified code is that a coded
string has the minimum possible size.

In the first line of the output file output the string s. It should consist of
the lowercase letters of the Latin alphabet. It is guaranteed that the length
of the correct answer does not exceed 104 symbols.
"""

import sys


class Tree(object):

    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def update(self, value, path):
        head = self
        for code in path:
            if code == '0':
                if head.left is None:
                    head.left = Tree()
                head = head.left
            else:
                if head.right is None:
                    head.right = Tree()
                head = head.right
        head.value = value

    def decode(self, cipher):
        message = ''
        head = self

        for code in cipher:
            if code == '0':
                head = head.left
            else:
                head = head.right
            if head.value:
                message += head.value
                head = self
        return message


def main():
    cipher = ''
    tree = Tree()

    _ = input()
    for line in sys.stdin:
        try:
            letter, code = line.rstrip().split(': ')
            tree.update(letter, code)
        except ValueError:
            cipher = line.rstrip()
    print(tree.decode(cipher))

if __name__ == '__main__':
    main()
