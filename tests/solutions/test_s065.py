import pytest

from solutions.s065 import solve


EXAMPLES = (
    ('text', 'expected'),
    [
        ('Everyone of us has all we need', 'Everyone'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert solve(text) == expected
