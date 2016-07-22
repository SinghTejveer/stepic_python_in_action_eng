import pytest

from solutions.s043 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([8, 35, 6, 44, 36, 64, 12, 89, 81], 54),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
