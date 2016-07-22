import pytest

from solutions.s040 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([7, 5], 35),
        ([15, 15], 15),
        ([12, 16], 48)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
