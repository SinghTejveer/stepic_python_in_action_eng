import pytest

from solutions.s049 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([3, 6, 8], 17),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
