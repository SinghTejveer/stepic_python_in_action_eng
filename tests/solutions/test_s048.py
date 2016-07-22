import pytest

from solutions.s048 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([0, -1, 0, 1, 1, 1, 1, 0, 0, 0, -1, 1], [5, 5, 2]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
