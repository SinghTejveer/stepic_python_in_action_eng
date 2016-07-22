import pytest

from solutions.s044 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([16, 18, 62, 36, 19, 12, 66, 68, 32, 14, 89, 8], 68),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
