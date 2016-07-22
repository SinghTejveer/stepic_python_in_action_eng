import pytest

from solutions.s192 import solve


EXAMPLES = (
    ('capacity', 'items', 'expected'),
    [
        (50, [(60, 20), (100, 50), (120, 30)], 180),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(capacity, items, expected):
    assert solve(capacity, items) == expected
