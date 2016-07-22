import pytest

from solutions.s087 import solve


EXAMPLES = (
    ('text', 'expected'),
    [
        ('Beautiful is better than ugly. Explicit is better than implicit.',
         [(2, 2), (4, 2), (5, 1), (6, 2), (8, 1), (9, 2)]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, expected):
    assert solve(text) == expected
