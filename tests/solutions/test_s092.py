import pytest

from solutions.s092 import solve


EXAMPLES = (
    ('intervals', 'expected'),
    [
        ([(1, 3), (2, 5), (3, 6)], [3]),
        ([(4, 7), (1, 3), (2, 5), (5, 6)], [3, 6]),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(intervals, expected):
    assert solve(intervals) == expected
