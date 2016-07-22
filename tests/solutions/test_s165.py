import pytest

from solutions.s165 import solve


EXAMPLES = (
    ('text', 'expected'),
    [
        ('kayak', True),
        ('world', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert solve(text) == expected
