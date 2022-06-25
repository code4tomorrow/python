def quicksort(arr, low, high):
    # Note: always partitions with the last element as the pivot

    i = low  # i is initialized to be the left side of our list

    for j in range(low, high):
        # if j is smaller than the pivot, arr[j] is smaller than the pivot,
        # so we want to move it to the left
        if arr[j] < arr[high]:
            # swaps arr[j] and arr[i], so arr[j] is at the left side of the list
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # move the pivot from the end to the correct location
    arr[i], arr[high] = arr[high], arr[i]

    quicksort(arr, low, i - 1)  # left side of the pivot
    quicksort(arr, i + 1, high)  # right side of the pivot
