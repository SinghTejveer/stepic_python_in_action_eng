"""The lucky ticket

Paul loves to ride public transport and after receiving the ticket, he
immediately checks whether he got the lucky one. A ticket is considered
a lucky one if the sum of the first three numbers in this ticket matches
the sum of the last three numbers in the same ticket.

However, Paul does not count well in head that is why he asks you to write
the program, which will check the equality of the sums and display "Lucky"
if the sums match, and "Regular" if the sums differ.

A string of six digits is provided as input to the program.

You need to print out only the word "Lucky" or "Regular" with a capital letter.
"""


def solve(num):
    return sum(int(x) for x in num[:3]) == sum(int(x) for x in num[3:])


def main():
    num = input().rstrip()
    print('Lucky' if solve(num) else 'Regular')

if __name__ == '__main__':
    main()
