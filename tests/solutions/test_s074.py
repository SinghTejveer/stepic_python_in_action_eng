import pytest

from solutions.s074 import solve


EXAMPLES = (
    ('text', 'substring', 'expected'),
    [
        ('abacabadaba', 'aba', [0, 4, 8]),
        ('aaaa', 'aa', [0, 1, 2]),
        ('abc', 'd', [-1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(text, substring, expected):
    assert solve(text, substring) == expected
