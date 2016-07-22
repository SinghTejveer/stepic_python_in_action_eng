import pytest

from solutions.s063 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ('acggtgttat', 40.0),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
