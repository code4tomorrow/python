def listsum(arr):
    total = 0

    for i in arr:
        if isinstance(i, list):
            total = total + listsum(i)
        else:
            total = total + i

    return total
