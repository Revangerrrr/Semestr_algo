import timeit
import random
import matplotlib.pyplot as plt


def almost_ordered(n: int) -> list:
    ord_size = int(n * 0.95)
    return [i for i in range(ord_size)] + [
        random.randint(-10, n) for _ in range(n - ord_size)
    ]


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
    x = almost_ordered(i)
    print(x)
    plt_x.append(len(x))

    pt = foo_timer.timeit(number=1)
    plt_y.append(pt)

plt.plot(plt_x, plt_y)
plt.show()