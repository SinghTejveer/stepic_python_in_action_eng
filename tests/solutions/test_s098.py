import pytest

from solutions.s098 import solve


EXAMPLES = (
    ('k', 'array', 'expected'),
    [
        (0, [3, 6, 5, 7, 2, 9, 8, 10, 4, 1], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(k, array, expected):
    solve(k, array, 0, len(array) - 1)
    assert array[k] == expected
