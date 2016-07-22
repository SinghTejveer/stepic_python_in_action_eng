import pytest

from solutions.s041 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([8, 24], 272),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
