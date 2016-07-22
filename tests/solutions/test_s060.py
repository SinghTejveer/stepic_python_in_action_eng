import pytest

from solutions.s060 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (7, 'NO'),
        (43, 'NO'),
        (18, 'YES'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(args) == expected
