import pytest

from solutions.s096 import solve


EXAMPLES = (
    ('array', 'expected'),
    [
        ([2, 3, 9, 2, 2], 1),
        ([1, 2, 3, 4, 5], 0),
        ([1, 1, 1, 2, 3, 4], 0),
        ([2, 989878533, 387770525, 2, 2, 2, 2, 66964391, 2, 944508853], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(array, expected):
    assert solve(array) == expected
