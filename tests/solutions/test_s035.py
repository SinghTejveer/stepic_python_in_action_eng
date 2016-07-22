import pytest

from solutions.s035 import solve

EXAMPLES = (
    ('args', 'expected'),
    [
        ((1, -1, -2), (-1, 2)),
        ((-11.0, -32.0, 41.0), (-3.8717701455106055, 0.9626792364196965)),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
