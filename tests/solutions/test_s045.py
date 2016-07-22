import pytest

from solutions.s045 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([4, 19, 96, 14, 44, 20], 62),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
