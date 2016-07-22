import pytest

from solutions.s172 import solve


EXAMPLES = (
    ('word1', 'word2', 'expected'),
    [
        ('silent', 'listen', True),
        ('AbaCa', 'AcaBa', True),
        ('abaca', 'acada', False),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(word1, word2, expected):
    assert solve(word1, word2) == expected
