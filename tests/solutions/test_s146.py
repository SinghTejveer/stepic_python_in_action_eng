import pytest

from solutions.s146 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        ([12, 179, 0, 5], [315, 43]),
        ([1, 1, 99, 1], [2, 0])
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
