# pylint: disable=invalid-name

import pytest

from solutions.s098 import (
    get_neighbors,
    get_min_available,
    solve
)


NEIGHBOURS = (
    ('args', 'expected'),
    [
        ([0, 3, 4], [1, 4]),
        ([1, 3, 4], [2, 5]),
        ([3, 3, 4], [7]),
        ([4, 3, 4], [5, 8]),
        ([5, 3, 4], [6, 9]),
        ([7, 3, 4], [11]),
        ([8, 3, 4], [9]),
        ([10, 3, 4], [11]),
        ([11, 3, 4], []),
    ]
)

AVAILABLE = (
    ('available', 'weights', 'expected'),
    [
        ([1, 2], [9, 2, 1, 5], 2),
    ]
)

EXAMPLES = (
    ('matrix', 'n', 'm', 'expected'),
    [
        ([1, 1, 1, 1, 5, 2, 2, 100, 9, 4, 2, 1], 3, 4, 8),
        ([1], 1, 1, 1),
        ([1, 2, 3, 4], 4, 1, 10),
        ([3, 2, 1, 2, 0, 3, 1, 2, 3], 3, 3, 10),
        ([1, 1, 1, 1], 2, 2, 3),
    ]
)


@pytest.mark.parametrize(*NEIGHBOURS)
def test_get_unvisited_neighbours(args, expected):
    assert get_neighbors(*args) == expected


@pytest.mark.parametrize(*AVAILABLE)
def test_get_min_available(available, weights, expected):
    assert get_min_available(available, weights) == expected


@pytest.mark.parametrize(*EXAMPLES)
def test_solve(matrix, n, m, expected):
    assert solve(matrix, n, m) == expected
