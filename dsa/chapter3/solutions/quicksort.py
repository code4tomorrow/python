lst = [-3, 5, -10, 18, 74, 22, 1, -40]


def quicksort(arr: list):
    """
    quicksort_recursive takes in the list you are sorting, the first index of
    the sublist you want to sort, and the last index of the sublist you want
    to sort, in that order

    For the first call to quicksort_recursive, the first index and last index
    should be 0 and the index to the last item of the list respectively

    Make a call to quicksort_recursive with the appropriate arguments below
    """
    quicksort_recursive(arr, 0, len(arr) - 1)


def quicksort_recursive(arr, low, high):
    """
    Arguments:
        arr: list, the entire list we are sorting,
        low: int, the first index of the sublist we are sorting
        high: int, the last index of the sublist we are sorting
    """
    # base case
    if low >= high:
        return

    pivot_index = partition(arr, low, high)

    # recursive calls
    """
    After the list has been partitioned around the pivot_index, we need to
    call quicksort_recursive on the two sublists: the one to the left of the
    pivot_index, and the one to the right

    We do this on the right side by setting the high index to one less than
    pivot_index, and on the left side by setting the low index to one higher
    than pivot_index

    Make calls to quicksort_recursive with the appropriate arguments below
    """
    quicksort_recursive(arr, low, pivot_index - 1)  # right side
    quicksort_recursive(arr, pivot_index + 1, high)  # left side


def partition(arr, low, high):
    """
    Partition takes a pivot (in our case, arr[high]), and accomplishes the
    following:
        All of the elements between low and high that are SMALLER than the
        pivot are placed to the LEFT of the pivot.
        Conversely, all elements between low and high that are LARGER than
        the pivot are placed to the RIGHT of the pivot
    This has the side effect that the location of pivot after the partition has
    taken place is the same as if the list was sorted. Of course, the areas to
    the left and right of the pivot are not yet sorted.
    """
    i = low  # initialize i to the left side of what we are sorting

    """
    Create a for loop that creates an index j, and loops through indexes low
    (inclusive) to high (exclusive)
    """
    for j in range(low, high):  # iterate through the list with arr[j]
        """
        In our loop, we are trying to find items (arr[j]) that are less than
        our pivot (arr[high]). If we find one, we want to swap our item
        (arr[j]) with arr[i], an item thats to the left side of our
        sublist. Then, we will increment i by one, so we don't continuously
        swap with same arr[i] over and over again.

        Create an if statement to do this below
        """
        if arr[j] < arr[high]:
            # swap arr[j] with arr[i] so arr[j] is at the left side
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    """
    Our pivot (arr[high]) is still on the right side of our sublist. Let's swap
    it with arr[i] so it moves to the right spot.
    """
    arr[i], arr[high] = arr[high], arr[i]

    # return the pivot_index
    return i


if __name__ == "__main__":
    quicksort(lst, 0, len(lst) - 1)
    print(lst)
