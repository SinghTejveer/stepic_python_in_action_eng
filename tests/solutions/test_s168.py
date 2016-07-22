import pytest

from solutions.s168 import solve


EXAMPLES = (
    ('variable', 'expected'),
    [
        ('my_first_class', 'MyFirstClass'),
        ('a', 'A'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(variable, expected):
    assert solve(variable) == expected
