import pytest

from solutions.s167 import solve


EXAMPLES = (
    ('num', 'expected'),
    [
        (5, '5 contigs'),
        (1, '1 contig'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(num, expected):
    assert solve(num) == expected
