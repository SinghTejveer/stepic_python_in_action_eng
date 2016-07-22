import pytest

from solutions.s176 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (['abcdefghijklmnopqrstuvwxyz', [2, 5, 8, 15]], ['cdef', 'ijklmnop']),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected
