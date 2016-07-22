"""
As input your program receives the three strings – s, a, b, consisting of
lowercase letters of the Latin alphabet.

In a single operation you can exchange all the occurrences of string a in s to
the string b.

For example, s = "abab", a = "ab", b = "ba", then after one operation the
string s will become "baba", after two operations – "bbaa", and all subsequent
operations will not change the string s.

You need to find out after what minimum number of operations the string s will
not contain occurrences of the string a, or to find out that it will not happen.

Output a single number – the minimum number of operations, after which the
string s will have no occurrences of the string a.

If after any number of operations the string s will still contain the
occurrences of a, output Impossible.
"""


def solve(text, old, new):
    if old != new and old in new:
        return -1
    count = 0
    while old in text:
        temp = text
        text = text.replace(old, new)
        if text == temp:
            return -1
        count += 1
    return count


def main():
    text = input().rstrip()
    old = input().rstrip()
    new = input().rstrip()

    result = solve(text, old, new)
    print(result if result != -1 else 'Impossible')

if __name__ == '__main__':
    main()
