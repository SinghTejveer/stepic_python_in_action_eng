import pytest

from solutions.s096 import solve


EXAMPLES = (
    ('num', 'expected'),
    [
        (4, [1, 3]),
        (6, [1, 2, 3]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert solve(num) == expected
