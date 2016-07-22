import pytest

from solutions.s183 import solve


EXAMPLES = (
    ('numbers', 'expected'),
    [
        ([30, 32, 43, 65, -32, 54, 34, -23, 11, 9],
         [39, 43, 20, 99, 22]),
        ([1, 2, 3, 4, 5],
         [6, 6, 3]),
        ([123],
         [123])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(numbers, expected):
    assert solve(numbers) == expected
