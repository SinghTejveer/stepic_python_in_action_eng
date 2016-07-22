import pytest

from solutions.s053 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([1, 7, 9, 0, 5], 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
