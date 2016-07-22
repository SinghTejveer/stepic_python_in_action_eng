import pytest

from solutions.s036 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([100, 2], 50.),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
