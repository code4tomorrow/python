def binary_search(lst, item):
    """
    Arguments:
        lst - a list sorted in ascending order
        item - the item that we want to find
    Returns:
        the idx of the item or -1 if not found
    """

    low_bound = 0
    upper_bound = len(lst) - 1

    # take the average, but make sure it's an integer
    cur_idx = (low_bound + upper_bound) // 2

    while low_bound <= upper_bound:
        if lst[cur_idx] == item:
            return cur_idx
        if lst[cur_idx] < item:
            # it was an undershot, so set this as the new lower bound
            low_bound = cur_idx + 1
        else:  # lst[cur_idx] > item)
            # it was an overshot, so set this as the new upper bound
            upper_bound = cur_idx - 1
        # update cur_idx
        cur_idx = (low_bound + upper_bound) // 2
    return -1
