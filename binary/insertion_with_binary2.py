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
    print(arr)
    return arr


arr = [30, 20, 80, 40, 50, 10, 60, 70, 90]
insertion_sort_with_bin_search(arr)
