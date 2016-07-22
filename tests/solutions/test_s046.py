import pytest

from solutions.s046 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([8, 16], [8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
