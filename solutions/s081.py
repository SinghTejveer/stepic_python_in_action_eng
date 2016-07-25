"""
Write a program, which asks the name of the user and than greets him.

Enter your name: Chuck
Hello Chuck

Python 3 uses the input() function to read from the keyboard.
"""


def main():
    name = input('Enter your name: ').rstrip()
    print('Hello %s' % name)

if __name__ == '__main__':
    main()
