import pytest

from solutions.s042 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([3, 4, 5, 3, 3, 4, 3, 3, 3, 2, 4, 2, 3, 3], [2, 8, 3, 1]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
