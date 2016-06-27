import pytest

from solutions.s137 import solve


EXAMPLES = (
    ('args', 'expected'),
    [
        (, ),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert solve(*args) == expected