import pytest

from solutions.s057 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (15, 3),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
