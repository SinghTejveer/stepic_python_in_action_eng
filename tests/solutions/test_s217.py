import pytest

from solutions.s217 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ((2, 1), 2),
        ((2, 2), 4),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
