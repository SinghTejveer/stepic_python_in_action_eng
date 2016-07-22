import pytest

from solutions.s037 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([-5, 12], 4.5),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
