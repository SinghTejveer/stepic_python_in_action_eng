import pytest

from solutions.s085 import solve


EXAMPLES = (
    ('filename', 'expected'),
    [
        ('my file name.txt', 'my_file_name.txt'),
        ('string     with        multi spaces', 'string_with_multi_spaces'),
        ('single', 'single'),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(filename, expected):
    assert solve(filename) == expected
