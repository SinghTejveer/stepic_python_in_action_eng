import pytest

from solutions.s062 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ('090234', True),
        ('123456', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
