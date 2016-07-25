import pytest

from solutions.s099 import solve


EXAMPLES = (
    ('sequence', 'expected'),
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 4, 4, 3, 5, 2, 8], [1, 4, 5, 8]),
        ([1, 3, 5, 2, 4], [1, 3, 5]),
        ([1, 100, 2, 3, 4], [1, 2, 3, 4]),
        ([16, 9, 29, 6, 6, 9, 24], [6, 9, 24])
    ])


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(sequence, expected):
    assert solve(sequence) == expected
