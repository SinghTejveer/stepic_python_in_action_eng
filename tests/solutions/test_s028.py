import pytest

from solutions.s028 import symmetrical

EXAMPLES = (
    ('number', 'expected'),
    [
        (2002, True),
        (2008, False),
        (123, False),
        (12, False),
        (1, False),
        (110, True),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(number, expected):
    assert symmetrical(number) == expected
