import pytest

from solutions.s157 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([1, 7, 9], 5.666666666666667),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
