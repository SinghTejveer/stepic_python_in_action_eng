import pytest

from solutions.s050 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (50, [1, 2, 4, 8, 16, 32]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
