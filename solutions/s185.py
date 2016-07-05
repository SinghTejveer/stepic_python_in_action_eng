"""
In the internet, each computer is assigned a four-byte code (IP address),
which is usually written as four numbers, each of which can take the values
from 0 to 255, separated by periods. Below are the examples of the correct
IP addresses:

127.0.0.0
192.168.0.1
255.0.255.255

Write a program to determine whether the specified spring is a correct IP
address.

The program should take a string of arbitrary characters as input. If this
string is a correct record of an IP address - output YES, otherwise - output NO.

Note

In order to convert string to number it is convenient to use the int function,
which takes one string as an argument and returns a number.
"""


def solve(ipv4: str) -> bool:
    parts = ipv4.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True


def main():
    ipv4 = input().rstrip()
    print('YES' if solve(ipv4) else 'NO')

if __name__ == '__main__':
    main()
