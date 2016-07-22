import pytest

from solutions.s007 import count_coins

EXAMPLES = (
    ('dollars', 'cents', 'pies', 'expected'),
    [
        (10, 15, 2, (20, 30)),
        (2, 50, 4, (10, 0)),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(dollars, cents, pies, expected):
    assert count_coins(dollars, cents, pies) == expected
