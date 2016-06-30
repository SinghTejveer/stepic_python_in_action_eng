import pytest

from solutions.s155 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([1, -3, 5, -6, -10, 13], 340),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
