import pytest

from solutions.s071 import solve


EXAMPLES = (
    ('grades', 'expected'),
    [
        (['F', 'B', 'A', 'A', 'B', 'C', 'A', 'D'], .38),
        (['B', 'C', 'B'], 0),
        (['A', 'D'], .5)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(grades, expected):
    assert solve(grades) == expected
