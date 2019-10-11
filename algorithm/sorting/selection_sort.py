import time
import random

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume i element is minimum
        min_index = i
        # Scan to find the real minimum number
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                # Change minimum index to real minimum element of current round
                min_index = j
        # Swap real minimum element to i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    # numbers = [4, 2, 5, 7, 1, 3]
    numbers = [random.randint(0, 1000) for _ in range(1000)]
    t0 = time.time()
    print(selection_sort(numbers))
    t1 = time.time()
    print('Elapse: {}'.format(t1-t0))
