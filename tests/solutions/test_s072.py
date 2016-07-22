import pytest

from solutions.s072 import solve


EXAMPLES = (
    ('command', 'expected'),
    [
        ('15.5 mile in km', '2.49e+01'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(command, expected):
    assert solve(command) == expected
