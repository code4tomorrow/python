def mergesort(lst: list) -> list:
    """
    Let's implement mergesort,
    First let's create a base case where if the list is 0 or 1 elements long,
    return it
    """
    # your code here

    """
    Now that we have handled the base case, if the list is any longer, we can
    go into typical mergesort logic,

    We need to split the list into 2 halves, so lets first find the middle
    index value. Use // instead of / because we want an integer
    """
    # your code here

    """
    Now we can run mergesort on the first and second halves of lst. Create a
    variable first_half which is the result of calling mergesort on the first
    half of lst. Repeat for the second half of the list, creating the variable
    second_half. Use list splicing for this.
    """
    # your code here

    """
    Now we need to merge the two sorted halves. In order to do this, we will
    implement a mergelists helper function. Return the result of mergelists
    with first_half and second_half as the two parameters.
    """
    return  # your code here


def mergelists(lst1: list, lst2: list) -> list:
    idx1 = 0
    idx2 = 0
    ret = []

    """
    Let's create a while loop that runs for as long as idx1 or idx2 is less
    than the len of lst1 or lst2.
    """
    while idx1 < len(lst1) or idx2 < len(lst2):
        # If both lists have items, we need to compare the first items of the
        # lst1 and lst2, and append whichever item is smaller to ret. Then, we
        # increment the idx1 or idx2 variable respectively
        if idx1 < len(lst1) and idx2 < len(lst2):
            # your code here
            pass

        elif idx1 < len(lst1):
            # if only lst1 has items left, append the remaining items to the
            # end of ret, and set idx1 to len(lst1)

            # your code here
            pass
        elif idx2 < len(lst2):
            # if only lst2 has items left, append the remaining items to the
            # end of ret, and set idx2 to len(lst2)

            # your code here
            pass
    return ret


if __name__ == "__main__":
    lst = [-3, 5, -10, 18, 74, 22, 1, -40]
    mergesort(lst)
    print(lst)
