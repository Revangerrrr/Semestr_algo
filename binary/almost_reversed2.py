import timeit
import matplotlib.pyplot as plt


def almost_reversed(n: int) -> list:
    res = [i - n / 2 for i in range(n, 0, -1)]
    res[n // 2], res[n // 2 + 1] = res[n // 2 + 1], res[n // 2]
    return res


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
    x = almost_reversed(i)
    print(x)
    plt_x.append(len(x))

    pt = foo_timer.timeit(number=1)
    plt_y.append(pt)

plt.plot(plt_x, plt_y)
plt.show()