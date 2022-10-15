def partitionv1(arr, pi):
    """
    partitionv1 takes some pivot index (pi), and puts all of the items
    smaller than pivot to the left, and all of the items larger than
    pivot to the right,

    in doing so we put pivot in the same spot as if the entire list was
    sorted

    note: this is only one way of doing it
    """
    # moves pivot to the end of the list so it doesn't get in the way
    arr[-1], arr[pi] = arr[pi], arr[-1]

    i = 0  # i is initialized to be the left side of our list

    for j in range(len(arr)):
        # if j is smaller than the pivot, arr[j] is smaller than the pivot,
        # so we want to move it to the left
        if arr[j] < arr[-1]:
            # swaps arr[j] and arr[i], so arr[j] is at the left side of the list
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # move the pivot from the end to the correct location
    arr[i], arr[-1] = arr[-1], arr[i]


def partitionv2(arr, low, high):
    """
    partitionv2 takes an array, a low, and a high and partitions
    the section of the array between low and high (inclusive).

    partitionv2 always partitions with the last element in the
    section as the pivot
    """

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


def quicksort(arr, low, high):
    """
    quicksort that recursively partitions the left nd right side
    of the pivot

    This implementation always partitions with the last element as the pivot
    """

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
