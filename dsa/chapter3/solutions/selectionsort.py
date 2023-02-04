def selectionsort(arr: list):
    """
    Let's implement selection sort! There are 4 easy steps to follow in order
    to implement it.
        1. Create a loop through iterate through the list.
        2. Create an inner loop that iterates from the outer index + 1 to the
           end of the list.
        3. Compare the element at the outer index to the element at the inner
           index.
        4. If the element at the outer index is larger than at the inner index,
           swap the 2 elements.
    """

    # Step 1, create an outer loop that iterates through the whole list. Let's
    # name the outer index "i"
    for i in range(len(arr)):
        # Step 2, create an inner loop that iterates from i+1 to the end of the
        # list, let's name inner index "j"
        for j in range(i + 1, len(arr)):
            # Step 3, check if the element at index i is larger than the
            # element at index j
            if arr[i] > arr[j]:
                # Step 4, swap the element at the outer index with the element
                # at the inner index
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    lst = [-3, 5, -10, 18, 74, 22, 1, -40]
    selectionsort(lst)
    print(lst)
