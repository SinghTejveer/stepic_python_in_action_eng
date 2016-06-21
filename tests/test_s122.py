import pytest

from solutions.s122 import square

EXAMPLES = (
    ('room_type', 'data', 'expected'),
    [
        ('rectangle', [4, 10], '40.0'),
        ('circle', [5], '78.5'),
        ('triangle', [3, 4, 5], '6.0'),
        ('triangle', [3, 3, 3], '3.897114317029974'),
        ('circle', [0], '0')
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(room_type, data, expected):
    assert square(room_type, data) == expected
