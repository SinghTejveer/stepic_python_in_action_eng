import pytest

from solutions.s138 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([-1, 1, -1, 1], [1]),
        ([0, 1, -6, 5], [1, 5]),
        ([1, 1, 1, 1], [])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
