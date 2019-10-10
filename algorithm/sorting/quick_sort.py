import time
import random


def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def quick_sort_pythonic(arr):
    lesser = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                lesser.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort_pythonic(lesser) + equal + quick_sort_pythonic(greater)
    else:
        return arr


if __name__ == '__main__':
    # numbers = [10, 7, 8, 9, 1, 5]
    numbers = [random.randint(0, 1000) for _ in range(1000)]
    t0 = time.time()
    print(quick_sort_pythonic(numbers))
    t1 = time.time()
    print('Elaspse: {}'.format(t1-t0))

    # n = len(numbers)
    # quick_sort(numbers, 0, n-1)
    # print(numbers)
