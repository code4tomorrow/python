def mergelists(lst1, lst2):
    idx1 = 0
    idx2 = 0
    ret = []

    # while either one has unused items
    while idx1 < len(lst1) or idx2 < len(lst2):
        # both lists still have items
        if idx1 < len(lst1) and idx2 < len(lst2):
            if lst1[idx1] < lst2[idx2]:
                ret.append(lst1[idx1])  # add the item from lst1
                idx1 += 1  # increment our idx in lst1
            else:  # lst2[idx2] <= lst1[idx1]
                ret.append(lst2[idx2])  # add the item from lst2
                idx2 += 1  # increment our idx in lst2

        # only one list still has items
        elif idx1 < len(lst1):  # if only lst1 still has items
            ret.extend(lst1[idx1:])  # add the rest of this list
            idx1 = len(lst1) + 1
        elif idx2 < len(lst2):  # if only lst2 still has items
            ret.extend(lst2[idx2:])  # add the rest of this list
            idx2 = len(lst2) + 1

    return ret


def mergesort(lst):
    # "base case" where the list is just 0 or 1 item(s).
    # In this case, we can say it is already sorted and just return it.
    if len(lst) <= 1:
        return lst

    # if it's not just 1 or 0 item(s), then follow mergesort logic
    middle_idx = len(lst) // 2  # we want an integer, so use //
    first_half = mergesort(lst[:middle_idx])  # sort the first half
    second_half = mergesort(lst[middle_idx:])  # sort the second half
    return mergelists(first_half, second_half)  # merge the two sorted halves


print(mergesort([5, 4, 3, 2, 1]))
print(mergesort([i for i in range(99, -1, -1)]))
