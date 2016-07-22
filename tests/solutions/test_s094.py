from collections import Counter
import pytest

from solutions.s094 import encode


EXAMPLES = (
    ('frequency', 'expected'),
    [
        (Counter('a'),
         [['a', '0']]),
        (Counter('abacabad'),
         [['a', '0'], ['b', '10'], ['c', '110'], ['d', '111']])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(frequency, expected):
    assert encode(frequency) == expected
