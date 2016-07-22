import pytest

from solutions.s052 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (1, 'YES'),
        (2, 'YES'),
        (3, 'NO'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
