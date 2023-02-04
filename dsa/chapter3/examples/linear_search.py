def linear_search(arr, val) -> int:
    """
    Search the provided array for the provided value
    and get the index, if found
    Arguments:
        arr - the array to search in
        val - the value to search for
    Returns:
        int - the index of the value if it was found, else -1
    """
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1
