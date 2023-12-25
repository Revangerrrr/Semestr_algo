def insertion_sort(some_list: list) -> list:
    shifts = 0  # число перестановок
    comparisons = 0

    for i in range(len(some_list)):
        j = i - 1
        key = some_list[i]
        while some_list[j] > key and j >= 0:
            comparisons += 1
            some_list[j + 1] = some_list[j]
            shifts += 1
            j -= 1
        some_list[j + 1] = key
        shifts += 1
        print(some_list)

    print("Число перестановок: ", shifts)
    print("Число сравнений: ", comparisons)
    return some_list


test = list([9, 8, 7, 6, 5, 4, 3, 2, 1])
test_list = list([7, 3, 9, 4, 2, 5, 6, 1, 8])
test_list_1 = [3, 5, 2, 9, 8, 1, 6, 4, 7]
print('Unsorted list: ', test_list)
insertion_sort(test_list)
print('Sorted list: ', end='')
print(test_list)
print('Unsorted list: ', test_list_1)
insertion_sort(test_list_1)
print('Sorted list: ', end='')
print(test_list_1)
insertion_sort(test)
print('Sorted list: ', end='')
print(test)
