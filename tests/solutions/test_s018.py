import pytest

from solutions.s018 import calculator

EXAMPLES = (
    ('num1', 'num2', 'math_operator', 'expected'),
    [
        (5, 0, 'mod', 'Division by 0!'),
        (5, 0, '/', 'Division by 0!'),
        (5, 0, 'div', 'Division by 0!'),
        (-12, -8, '*', '96.0'),
        (5, 10, '/', '0.5'),
        (2, 3, '+', '5.0'),
        (3, 2, '-', '1.0'),
        (2, 3, '-', '-1.0'),
        (2, 3, 'pow', '8.0'),
        (5, 2, 'mod', '1.0'),
        (5, 2, 'div', '2.0'),
        (2, 3, '/', '0.6666666666666666'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num1, num2, math_operator, expected):
    assert calculator(num1, num2, math_operator) == expected
