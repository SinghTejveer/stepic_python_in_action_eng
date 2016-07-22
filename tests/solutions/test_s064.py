import pytest

from solutions.s064 import solve


EXAMPLES = (
    ('dna', 'expected'),
    [
        ('aaaabbcaa', 'a4b2c1a2'),
        ('abc', 'a1b1c1'),
        ('a', 'a1'),
        ('', ''),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(dna, expected):
    assert solve(dna) == expected
