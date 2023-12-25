import timeit
import matplotlib.pyplot as plt


def almost_reversed(n: int) -> list:
    res = [i - n / 2 for i in range(n, 0, -1)]
    res[n // 2], res[n // 2 + 1] = res[n // 2 + 1], res[n // 2]
    return res


def insertion_sort(some_list: list) -> list:
    for i in range(len(some_list)):
        j = i - 1
        key = some_list[i]
        while some_list[j] > key and j >= 0:
            some_list[j + 1] = some_list[j]
            j -= 1
        some_list[j + 1] = key
    return some_list


foo_timer = timeit.Timer('insertion_sort(x)', globals=globals())

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