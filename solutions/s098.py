"""
Given non-negative integers n, k and array of integers from the range of
[0..10^9] size n <= 10^6. You need to find the k-th order statistics, i.e.
to print the number, which would reside on the position with the index k
(0..n-1) in the sorted array. Write a non-recursive algorithm using the
"divide and conquer" method.

Requirements for the additional memory: O(n).
Required average time complexity: O(n).

The Partition function should be implemented using two iterators passing in the
single direction from the start to the end of the array:

- Selected the reference element. The reference element is changed by the last
  element of the array.
- During the execution of the Partition function, the beginning of the array
  contains the elements, which are not larger than the reference one. Next
  placed the elements, which are strictly larger than the reference one.
  The end of the array contains unconsidered elements.
  The last element - reference element.
- Iterator (index) i specifies the beginning of the elements group, which are
  strictly larger than the reference one.
- Iterator j is larger than i, iterator j specifies the first unconsidered
  element.
- Algorithm step. Consider the element, which is specified by j. If it is
  larger than the reference element, we move j. If it is not grater than the
  reference one, we swap a[i] and a[j], move i and move j.
- At the end of the algorithm execution we change the reference element to the
  one, specified by iterator i.

Sample Input:
    10 0
    3 6 5 7 2 9 8 10 4 1

Sample Output:
    1
"""


def partition(array, left, right):
    pivot = array[left]
    j = left
    same = 0  # Учет количества опорных
    for i in range(left + 1, right + 1):
        # Если следующий элемент больше опорного, то все в порядке
        if array[i] > pivot:
            continue
        # Если следующий элемент равен опорному, то меняем его с местами
        # с первым большим опорного (добавляем в цепочку опорных)
        elif array[i] == pivot:
            array[i], array[j + same + 1] = array[j + same + 1], array[i]
            same += 1  # Еще один равный опорному
        # Если следующий элемент меньше опорного
        else:
            # Меняем местами с первым опорным
            array[i], array[j] = array[j], array[i]
            j += 1
            # Если между найденным меньшим и последним опорным есть элементы
            # больше опорного, то последний передвинутый опорный меняем местами
            # с первым большим опорного
            if j + same != i:
                array[i], array[j + same] = array[j + same], array[i]
    return j, j + same


def solve(k, array, left, right):
    if left >= right:
        return
    med1, med2 = partition(array, left, right)
    if k < med1:
        solve(k, array, left, med1 - 1)
    elif k > med2:
        solve(k, array, med2 + 1, right)


def main():
    _, k = [int(x) for x in input().rstrip().split()]
    array = [int(x) for x in input().rstrip().split()]
    solve(k, array, 0, len(array) - 1)
    print(array[k])

if __name__ == '__main__':
    main()
