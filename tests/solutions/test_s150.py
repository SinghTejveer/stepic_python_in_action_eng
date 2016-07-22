import pytest

from solutions.s150 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (50, [1, 4, 9, 16, 25, 36, 49]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
