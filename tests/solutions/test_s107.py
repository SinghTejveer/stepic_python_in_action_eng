import pytest

from solutions.s107 import count_desks

EXAMPLES = (
    ('groups', 'expected'),
    [
        ([20, 21, 22], 32),
        ([16, 18, 20], 27),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(groups, expected):
    assert count_desks(*groups) == expected
