# pylint: disable=invalid-name

"""
Each square of the rectangular table NxM contains some number.

Initially the player is located in the top left square.

In one move he is allowed to move to the neighbouring cell either to the right
or down (left and upward moves are not permitted). When passing through
a square the player pays that amount of coins, which is written in this square
(he must also pay coins for the first and for the last squares of his path).

You need to find the minimum number of coins, which the player needs to take
in order to get to the bottom right corner.

First line has the two numbers N и M — the size of the table (1<=N<=20,
1<=M<=20). Next go N lines having M numbers in each — the number of coins
to pass through the corresponding squares (integers from 0 to 100).

Sample Input 1:
    3 4
    1 1 1 1
    5 2 2 100
    9 4 2 1
Sample Output 1:
    8

Sample Input 2:
    1 1
    1
Sample Output 2:
    1
"""


def get_neighbors(index, n, m):
    result = []
    if (index + 1) % m != 0:
        result.append(index + 1)  # Right
    if index < (n - 1)*m:
        result.append(index + m)  # Down
    return result


def get_not_visited_neighbors(current, n, m, visited):
    neighbors = get_neighbors(current, n, m)
    return [neighbor for neighbor in neighbors if not visited[neighbor]]


def get_min_available(available, weights):
    min_available = min(available, key=lambda index: weights[index])
    available.remove(min_available)
    return min_available


def solve(matrix, n, m):
    available = []
    visited = [False]*n*m
    weights = [float('inf')]*n*m
    weights[0] = matrix[0]
    current = 0

    while current != n*m - 1:
        visited[current] = True
        neighbors = get_not_visited_neighbors(current, n, m, visited)
        for neighbor in neighbors:
            new_weight = weights[current] + matrix[neighbor]
            weights[neighbor] = min(weights[neighbor], new_weight)
            if not visited[neighbor] and neighbor not in available:
                available.append(neighbor)
        current = get_min_available(available, weights)

    return weights[current]


def main():
    n, m = [int(x) for x in input().rstrip().split()]
    matrix = []
    for _ in range(n):
        row = [int(cell) for cell in input().rstrip().split()]
        matrix.extend(row)
    print(solve(matrix, n, m))

if __name__ == '__main__':
    main()
