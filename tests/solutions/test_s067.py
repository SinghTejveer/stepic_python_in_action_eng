import pytest

from solutions.s067 import solve


EXAMPLES = (
    ('text', 'expected'),
    [
        ('In the town where I was born', 7),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert solve(text) == expected
