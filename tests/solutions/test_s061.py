import pytest

from solutions.s061 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (6188989133, 13),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
