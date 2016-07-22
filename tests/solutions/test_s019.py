import pytest

from solutions.s019 import min_distance

EXAMPLES = (
    ('data', 'expected'),
    [
        ([23, 52, 8, 43], 8),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(data, expected):
    assert min_distance(*data) == expected
