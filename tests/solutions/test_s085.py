import pytest

from solutions.s085 import solve


EXAMPLES = (
    ('ipv4', 'expected'),
    [
        ('127.0.0.1', True),
        ('256.0.0.1', False),
        ('255.0.0.1', True),
        ('1.2.3', False),
        ('1.2.3.4.5', False),
        ('-1.2.3.4', False)
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(ipv4, expected):
    assert solve(ipv4) == expected
