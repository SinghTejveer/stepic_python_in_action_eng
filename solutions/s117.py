"""Calculator

Write a simple calculator that reads the three input lines: the first number,
the second number and the operation, after which it applies the operation
to the entered numbers ("first number" "operation" "second number") and outputs
the result to the screen. Note that the numbers can be real.

Supported operations: +, -, /, *, mod, pow, div; where
    mod — taking the residue,
    pow — exponentiation,
    div — integer division.

If a user performs the division and the second number is 0, it is necessary to
output the line "Division by 0!".

Sample Input 1:
    5.0
    0.0
    mod
Sample Output 1:
    Division by 0!

Sample Input 2:
    -12.0
    -8.0
    *
Sample Output 2:
    96.0

Sample Input 3:
    5.0
    10.0
    /
Sample Output 3:
    0.5
"""

import operator

FUNCS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    'mod': operator.mod,
    'pow': operator.pow,
    'div': operator.floordiv
}


def calculator(num1, num2, math_operator):
    try:
        result = FUNCS[math_operator](num1, num2)
        if result % 1 != 0:
            return str(result)
        else:
            return '%0.1f' % result

    except ZeroDivisionError:
        return 'Division by 0!'


def main():
    num1 = float(input().rstrip())
    num2 = float(input().rstrip())
    math_operator = input().rstrip()
    print(calculator(num1, num2, math_operator))

if __name__ == '__main__':
    main()
