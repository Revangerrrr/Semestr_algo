import timeit
import matplotlib.pyplot as plt
import random


def almost_ordered(n: int) -> list:
    ord_size = int(n * 0.95)
    return [i for i in range(ord_size)] + [
        random.randint(-10, n) for _ in range(n - ord_size)
    ]


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start + 1 == end:
        return start + 1

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid)
    else:
        return mid


def insertion_sort_with_bin_search(arr: list):
    for i in range(1, len(arr)):
        if arr[i] <= arr[0]:
            index = 0
        elif arr[i] >= arr[i - 1]:
            continue
        else:
            index = binary_search(arr[0:i], arr[i], 0, i - 1)
        arr = arr[:index] + [arr[i]] + arr[index:i] + arr[i + 1:]
    return arr


foo_timer = timeit.Timer('insertion_sort_with_bin_search(x)', globals=globals())

plt_x = []
plt_y = []

for i in [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]:
    x = almost_ordered(i)
    print(x)
    plt_x.append(len(x))

    pt = foo_timer.timeit(number=1)
    plt_y.append(pt)

plt.plot(plt_x, plt_y)
plt.show()