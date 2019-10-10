import time
import random


def bubble_sort(arr):
    n = len(arr)
    # Loop through all element
    for i in range(n):
        # n-i-1:
        # "n-i": Last i elements are already sorted
        # "-1": The loop below will use "j+1", so "-1" is to limits the boundary
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap(Pythonic)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(arr)
    return arr


def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            # print(arr)
        if not swapped:
            break
    return arr


if __name__ == '__main__':
    # numbers = [1, 2, 3, 4, 5]
    numbers = [random.randint(0, 1000) for _ in range(1000)]
    t0 = time.time()
    print(bubble_sort(numbers))
    t1 = time.time()
    print("Elapse: {}".format(t1-t0))

    t0 = time.time()
    print(bubble_sort_optimized(numbers))
    t1 = time.time()
    print("Elapse: {}".format(t1-t0))
