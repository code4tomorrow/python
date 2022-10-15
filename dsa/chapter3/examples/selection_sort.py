def selection_sort(lst):
    for i in range(len(lst)):
        min_value = lst[i]
        min_val_idx = i

        # find the new minimum value and its idx
        for x in range(i, len(lst)):
            if lst[x] < min_value:
                min_value = lst[x]
                min_val_idx = x

        # swap the minimum value with the value at the current idx
        lst[i], lst[min_val_idx] = min_value, lst[i]
    return lst


test1 = [3, 12, 7, 2, 0, 3]
test1 = selection_sort(test1)
print(test1)  # [0, 2, 3, 3, 7, 12]

test2 = [-23, 0, 72, -33, 11, 6, 2, -5, -9, 10, -1]
test2 = selection_sort(test2)
print(test2)  # [-33, -23, -9, -5, -1, 0, 2, 6, 10, 11, 72]

test3 = [i for i in range(1000, -1, -1)]
test3 = selection_sort(test3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
print(test3)
