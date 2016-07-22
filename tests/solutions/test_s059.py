import pytest

from solutions.s059 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([1, 7, 9], 4.163331998932266),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
