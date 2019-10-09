from random import randint


def bubble_sort(arr):
    n = len(arr)
    # Loop through all element
    for i in range(n):
        # n -i - 1:
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap(Pythonic)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    numbers = [2, 7, 4, 1, 5, 3]
    nums = randint(1, 100)
    print(nums)
    print(bubble_sort(numbers))
