import pytest

from solutions.s154 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (7, [1, 2, 2, 3, 3, 3, 4]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
