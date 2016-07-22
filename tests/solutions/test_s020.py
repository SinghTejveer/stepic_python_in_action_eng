import pytest

from solutions.s020 import is_triangle

EXAMPLES = (
    ('sides', 'expected'),
    [
        ([3, 4, 5], 'YES'),
        ([3, 3, 3], 'YES'),
        ([1, 2, 9], 'NO')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(sides, expected):
    assert is_triangle(*sides) == expected
