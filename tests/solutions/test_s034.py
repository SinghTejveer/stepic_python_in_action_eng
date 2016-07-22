import pytest

from solutions.s034 import interest

EXAMPLES = (
    ('data', 'expected'),
    [
        ((12, 179, 0), (200, 48)),
        ((17, 94, 41), (110, 45)),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(data, expected):
    assert interest(*data) == expected
