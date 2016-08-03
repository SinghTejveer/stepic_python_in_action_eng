"""Calculator

You have a basic calculator, which has only three operations with the current
number x: replace x by 2x, 3x or x+1. Given the integer 1 <= n <= 10^5, find
the minimum number of k operations, necessary to get n from 1. Output k and
the sequence of intermediate numbers.

Sample Input 1:
    1
Sample Output 1:
    0
    1

Sample Input 2:
    5
Sample Output 2:
    3
    1 2 4 5

Sample Input 3:
    96234
Sample Output 3:
    14
    1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
"""


class Node(object):

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def generate_children(self):
        children = [Node(self.value - 1, self)]
        if self.value % 2 == 0:
            children.append(Node(self.value//2, self))
        if self.value % 3 == 0:
            children.append(Node(self.value//3, self))
        return children

    def __repr__(self):
        return 'Node({})'.format(self.value)


def generate_sequence(node):
    seq = []
    while node.parent is not None:
        seq.append(node.value)
        node = node.parent
    seq.append(node.value)
    return seq


def solve(number):
    if number == 1:
        return [1]

    nodes = [Node(number)]
    while nodes:
        generation = []
        for node in nodes:
            children = node.generate_children()
            for child in children:
                if child.value == 1:
                    return generate_sequence(child)
            generation.extend(children)
        nodes = generation


def main():
    number = int(input())
    result = solve(number)
    print(len(result) - 1)
    for item in result:
        print(item, end=' ')

if __name__ == '__main__':
    main()
