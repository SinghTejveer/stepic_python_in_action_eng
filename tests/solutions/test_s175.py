import pytest

from solutions.s175 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (['ababa', 'a', 'b'], 1),
        (['ababa', 'b', 'a'], 1),
        (['ababa', 'c', 'c'], 0),
        (['ababac', 'c', 'c'], -1),
        (['ababa', 'aba', 'cabab'], -1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
