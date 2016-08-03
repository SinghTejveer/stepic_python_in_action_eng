import pytest

from solutions.s100 import solve


EXAMPLES = (
    ('number', 'expected'),
    [
        (1, [1]),
        # (5, [1, 2, 4, 5]),
        # (10, [1, 3, 9, 10]),
        # (96234, [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039,
        #          32078, 96234]),
        # (32718, [1, 2, 4, 8, 24, 25, 75, 225, 226, 227, 454, 1362, 1363, 2726,
        #          5452, 5453, 10906, 32718]),
        # (98734, [])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert solve(number) == expected
